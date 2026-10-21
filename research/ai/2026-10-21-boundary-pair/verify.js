function verifyBoundary(m) {
  if (!Number.isInteger(m) || m < 3) throw Error("m must be an integer >= 3");
  const n=m-1, len=2*m+2, vec=()=>Array(len).fill(0n);
  const mono=(k,c=1n)=>{let a=vec();a[k]=c;return a;};
  const plus=(...vs)=>vs.reduce((a,v)=>a.map((x,i)=>x+v[i]),vec());
  const neg=v=>v.map(x=>-x);
  const shift=(v,k)=>v.map((_,j)=>j>=k?v[j-k]:0n);
  const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
  const assert=(b,s)=>{if(!b)throw Error("m="+m+": "+s);};
  const U=[];for(let i=2;i<=m-2;i++)U.push(mono(i));
  U.push(plus(mono(1),mono(m-1)),plus(mono(0),mono(1),mono(m)),plus(mono(1),mono(m+1)));
  const E0=plus(mono(0),mono(m,-1n),mono(2*m));
  const E1=plus(mono(1),mono(m-1,-1n),mono(m,-1n),mono(m+1,-1n),mono(2*m-1),mono(2*m,2n),mono(2*m+1));
  const d=[],e=[];for(let i=2;i<=m-2;i++){d.push(mono(i));e.push(mono(m+i));}
  d.push(mono(m-1),mono(0),plus(mono(1),mono(0,-1n),mono(m-1,-1n)));
  e.push(mono(2*m-1),mono(2*m),mono(2*m+1));
  for(let i=0;i<m;i++)for(let j=0;j<m;j++){
    assert(dot(d[i],U[j])===BigInt(i===j),"d(U)");
    assert(dot(e[i],shift(U[j],m))===BigInt(i===j),"e(t^m U)");
    assert(dot(d[i],shift(U[j],m))===0n && dot(e[i],U[j])===0n,"cross duals");
  }
  for(const u of U)for(const E of [E0,E1])
    assert(dot(E,u)===0n && dot(E,shift(u,m))===0n,"negative coefficient");
  const R=[plus(U[m-3],neg(U[m-2]))];
  for(let j=2;j<=m-2;j++)R.push(mono(m-j));
  R.push(U[m-2],U[m-1]);
  const J=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>BigInt(Math.abs(i-j)<=1)));
  for(let i=0;i<m;i++)for(let j=0;j<n;j++){
    const A=dot(E0,shift(R[i],j+1)), B=dot(E1,shift(R[i],j+1));
    assert(A===(i<n?-BigInt(i===j):0n),"boundary A");
    assert(B===(i<n?-J[i][j]:BigInt(j===n-1)),"boundary B");
  }
  for(let j=0;j<n;j++){
    const L=plus(d[j],e[j+1]);
    for(let i=0;i<m;i++){
      assert(dot(L,U[i])===BigInt(i===j),"upper first column");
      assert(dot(L,shift(U[i],m))===BigInt(i===j+1),"upper second column");
    }
  }
  let v=Array(n).fill(0n);v[n-1]=1n;
  const columns=[];
  for(let k=0;k<n;k++){columns.push(v);v=J.map(row=>dot(row,v));}
  const K=Array.from({length:n},(_,i)=>columns.map(c=>c[i]));
  let sign=1n,prev=1n;
  for(let k=0;k<n-1;k++){
    let p=k;while(p<n&&K[p][k]===0n)p++;
    assert(p<n,"Krylov pivot");
    if(p!==k){[K[p],K[k]]=[K[k],K[p]];sign=-sign;}
    const pivot=K[k][k];
    for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
      const num=K[i][j]*pivot-K[i][k]*K[k][j];
      assert(num%prev===0n,"Bareiss division");K[i][j]=num/prev;
    }
    for(let i=k+1;i<n;i++)K[i][k]=0n;
    prev=pivot;
  }
  const determinant=sign*K[n-1][n-1];assert(determinant===1n||determinant===-1n,"unimodular Krylov");
  return {m,source:[m+2,m+1],sharedDimension:m,negativeCoefficientsZero:true,upperConvolution:true,boundaryMatricesVerified:true,krylovDeterminant:String(determinant)};
}
console.log(JSON.stringify(Array.from({length:18},(_,i)=>verifyBoundary(i+3)),null,2));
