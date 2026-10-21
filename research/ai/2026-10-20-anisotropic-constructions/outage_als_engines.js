// Numerical exploration engines used while local execution was unavailable.
// Discovery code only; residuals do not establish an exact tensor identity.
function makeTarget(sizes){let offset=0,pts=[];for(const n of sizes){for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++)pts.push([offset+i*n+j,offset+j*n+k,offset+k*n+i]);offset+=n*n;}return {d:offset,pts};}

function buildProblem(source,N,target){
 const d=target.d,D=d*d;
 function contraction(maps,axis){const others=[0,1,2].filter(x=>x!==axis),left=maps[others[0]],right=maps[others[1]],M=new Float64Array(N*D);
 for(const pt of source){const x=pt[axis],y=pt[others[0]],z=pt[others[1]],off=x*D;for(let i=0;i<d;i++){const v=left[i*N+y];if(v===0)continue;for(let j=0;j<d;j++)M[off+i*d+j]+=v*right[j*N+z];}}return M;}
 function update(maps,axis,ridge=1e-12){const M=contraction(maps,axis),G=new Float64Array(N*N),R=new Float64Array(d*N),others=[0,1,2].filter(x=>x!==axis);
 let trace=0;for(let r=0;r<N;r++)for(let s=0;s<=r;s++){let v=0;for(let c=0;c<D;c++)v+=M[r*D+c]*M[s*D+c];G[r*N+s]=G[s*N+r]=v;if(s===r)trace+=v;}
 for(const pt of target.pts){const r=pt[axis],c=pt[others[0]]*d+pt[others[1]];for(let n=0;n<N;n++)R[r*N+n]+=M[n*D+c];}
 const L=new Float64Array(N*N),regularizer=Math.max(trace/N,1e-12)*ridge;
 for(let i=0;i<N;i++)for(let j=0;j<=i;j++){let s=G[i*N+j]+(i===j?regularizer:0);for(let k=0;k<j;k++)s-=L[i*N+k]*L[j*N+k];L[i*N+j]=i===j?Math.sqrt(Math.max(s,regularizer*1e-4)):s/L[j*N+j];}
 const result=new Float64Array(d*N),v=new Float64Array(N);
 for(let row=0;row<d;row++){for(let i=0;i<N;i++){let s=R[row*N+i];for(let j=0;j<i;j++)s-=L[i*N+j]*v[j];v[i]=s/L[i*N+i];}for(let i=N-1;i>=0;i--){let s=v[i];for(let j=i+1;j<N;j++)s-=L[j*N+i]*result[row*N+j];result[row*N+i]=s/L[i*N+i];}}
 maps[axis]=result;
 }
 function residual(maps){const M=contraction(maps,0),T=new Float64Array(d*D);for(let r=0;r<d;r++)for(let n=0;n<N;n++){const v=maps[0][r*N+n];for(let c=0;c<D;c++)T[r*D+c]+=v*M[n*D+c];}for(const [x,y,z]of target.pts)T[x*D+y*d+z]-=1;return Math.sqrt(T.reduce((s,x)=>s+x*x,0)/target.pts.length);}
 function normalize(maps){const norms=maps.map(m=>Math.sqrt(m.reduce((s,x)=>s+x*x,0))),g=Math.exp(norms.reduce((s,x)=>s+Math.log(x),0)/3);maps.forEach((m,i)=>{for(let j=0;j<m.length;j++)m[j]*=g/norms[i];});return norms;}
 return{d,N,update,residual,normalize};
}

function randomMaps(d,N,seed){let s=seed|0;const rand=()=>{s^=s<<13;s^=s>>>17;s^=s<<5;return(s>>>0)/4294967296;};return Array.from({length:3},()=>Float64Array.from({length:d*N},()=>2*(rand()-.5)/Math.sqrt(N)));}

function buildFastProblem(source,N,target){
 const d=target.d,groups=Array.from({length:3},()=>Array.from({length:N},()=>[])),tt=Array.from({length:3},()=>[]);
 for(let axis=0;axis<3;axis++){const other=[0,1,2].filter(i=>i!==axis);for(const pt of source)groups[axis][pt[axis]].push(pt[other[0]],pt[other[1]]);tt[axis]=target.pts.map(pt=>[pt[axis],pt[other[0]],pt[other[1]]]);}
 function gram(m){const G=new Float64Array(N*N);for(let i=0;i<N;i++)for(let j=0;j<=i;j++){let z=0;for(let k=0;k<d;k++)z+=m[i*d+k]*m[j*d+k];G[i*N+j]=G[j*N+i]=z;}return G;}
 function update(maps,axis,ridge=1e-12){
 const other=[0,1,2].filter(i=>i!==axis),B=maps[other[0]],C=maps[other[1]],GB=gram(B),GC=gram(C),G=new Float64Array(N*N),R=new Float64Array(N*d),group=groups[axis];
 for(let x=0;x<N;x++)for(let y=0;y<=x;y++){const left=group[x],right=group[y];let z=0;for(let i=0;i<left.length;i+=2){const offB=left[i]*N,offC=left[i+1]*N;for(let j=0;j<right.length;j+=2)z+=GB[offB+right[j]]*GC[offC+right[j+1]];}G[x*N+y]=G[y*N+x]=z;}
 const terms=tt[axis];for(let x=0;x<N;x++){const pairs=group[x],off=x*d;for(let i=0;i<pairs.length;i+=2){const offB=pairs[i]*d,offC=pairs[i+1]*d;for(let k=0;k<terms.length;k++){const [a,b,c]=terms[k];R[off+a]+=B[offB+b]*C[offC+c];}}}
 let trace=0;for(let i=0;i<N;i++)trace+=G[i*N+i];const reg=Math.max(trace/N,1e-12)*ridge,L=new Float64Array(N*N);
 for(let i=0;i<N;i++)for(let j=0;j<=i;j++){let z=G[i*N+j]+(i===j?reg:0);for(let k=0;k<j;k++)z-=L[i*N+k]*L[j*N+k];L[i*N+j]=i===j?Math.sqrt(Math.max(z,reg*1e-5)):z/L[j*N+j];}
 const A=R.slice();for(let i=0;i<N;i++){for(let j=0;j<i;j++){const l=L[i*N+j];for(let k=0;k<d;k++)A[i*d+k]-=l*A[j*d+k];}const l=L[i*N+i];for(let k=0;k<d;k++)A[i*d+k]/=l;}
 for(let i=N-1;i>=0;i--){for(let j=i+1;j<N;j++){const l=L[j*N+i];for(let k=0;k<d;k++)A[i*d+k]-=l*A[j*d+k];}const l=L[i*N+i];for(let k=0;k<d;k++)A[i*d+k]/=l;}
 let dot=0,norm=0;for(let i=0;i<N;i++){for(let k=0;k<d;k++)dot+=A[i*d+k]*R[i*d+k];for(let j=0;j<N;j++){let v=0;for(let k=0;k<d;k++)v+=A[i*d+k]*A[j*d+k];norm+=G[i*N+j]*v;}}
 maps[axis]=A;return Math.sqrt(Math.max(0,1+(norm-2*dot)/target.pts.length));
 }
 function normalize(maps){const norms=maps.map(m=>Math.sqrt(m.reduce((s,x)=>s+x*x,0))),g=Math.exp(norms.reduce((s,x)=>s+Math.log(x),0)/3);maps.forEach((m,i)=>{for(let j=0;j<m.length;j++)m[j]*=g/norms[i];});return norms;}
 return{N,d,update,normalize};
}

