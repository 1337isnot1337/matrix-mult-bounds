function verifyBlocks(m,b,G,Zseq){
 const a=m+1,n=m*(m+1)/2,J=Array.from({length:a},(_,i)=>i).filter(i=>i!==2);
 G=G.map((g,p)=>Array.from({length:b-p},(_,j)=>g[j]??0));
 Zseq=Zseq.map((z,q)=>Array.from({length:b+m+q},(_,j)=>z[j]??0));
 const H=J.map(d=>Array.from({length:m},(_,k)=>+(d+k===m-1)-+(d+k===m)));
 const W=H.map((r,i)=>[...r,...Array.from({length:m},(_,j)=>+(i===j))]);let det=1;
 for(let k=0;k<m;k++){
  let p=k;while(p<m&&!W[p][k])p++;if(p===m)throw Error("singular H");
  if(p!==k){[W[p],W[k]]=[W[k],W[p]];det=-det;}
  const v=W[k][k];if(Math.abs(v)!==1)throw Error("nonunit pivot");det*=v;W[k]=W[k].map(x=>x/v);
  for(let i=0;i<m;i++)if(i!==k){const t=W[i][k];W[i]=W[i].map((x,j)=>x-t*W[k][j]);}
 }
 const A=W.map(r=>Array.from({length:a},(_,i)=>i===2?0:r[m+J.indexOf(i)]));
 const nodes=[],Y=[],Z=[];
 for(let p=0;p<m;p++)for(let k=0;k<=p;k++){
  nodes.push([k,p-k]);Y.push(Array.from({length:b},(_,j)=>G[p][j-k]??0));Z.push(Zseq[p].slice(k,k+a+b-1));
 }
 let equations=0;
 for(let p=0;p<m;p++)for(let q=0;q<m-p;q++){
  const shifts=new Set;for(const d of J)for(let k=0;k<=p+q;k++)shifts.add(d+k);
  for(const ell of shifts){
   let value=0;for(let j=0;j<b-p;j++)value+=G[p][j]*Zseq[q][j+ell];
   const expected=p+q===m-1?(+(ell===m-1)-+(ell===m)):0;
   if(value!==expected)throw Error(JSON.stringify({m,p,q,ell,value,expected}));equations++;
  }
 }
 let negative=0,constant=0,retained=0,positive=0;const counts={};for(let e=1;e<m;e++)counts[e]=0;
 for(let x=0;x<m;x++)for(let y=0;y<n;y++)for(let z=0;z<n;z++){
  let value=0;for(let i=0;i<a;i++)for(let j=0;j<b;j++)value+=A[x][i]*Y[y][j]*Z[z][i+j];
  if(!Number.isSafeInteger(value))throw Error("unsafe arithmetic");
  const exponent=nodes[y][0]+nodes[y][1]+nodes[z][0]+nodes[z][1]-(m-1);
  if(exponent<0){if(value)throw Error("negative source coefficient");negative++;}
  else if(exponent===0){const expected=+(x===nodes[y][0]+nodes[z][0]);if(value!==expected)throw Error("constant source coefficient");constant++;retained+=expected;}
  else if(value){positive++;counts[exponent]++;}
 }
 function rank2(M){
  const basis=new Map;
  for(const row of M){
   let v=row.reduce((s,x,j)=>s|((BigInt(x)&1n)<<BigInt(j)),0n);
   while(v){const k=v.toString(2).length-1;if(basis.has(k))v^=basis.get(k);else{basis.set(k,v);break;}}
  }return basis.size;
 }
 const ranks=[rank2(A),rank2(Y),rank2(Z)];
 if(JSON.stringify(ranks)!==JSON.stringify([m,n,n]))throw Error("map ranks");
 const witness={source:[a,b],m,target:"canonical T"+m,a_map:A,y:Y,z:Z,block_factors:G,block_moments:Zseq,shared_hankel_matrix:H,shared_hankel_determinant:det,weights_x:Array(m).fill(1-m),weights_y:nodes.map(p=>p[0]+p[1]),weights_z:nodes.map(p=>p[0]+p[1]),coefficient_ring:"integers",improves_omega:false};
 const report={status:"exact integer full-source coefficient replay passed",source:"C("+a+","+b+")",source_dimensions:[a,b,a+b-1],target:"canonical T"+m,target_dimensions:[m,n,n],coefficient_ring:"integers; specializes to every field",source_monomials:a*b,target_coefficient_positions:m*n*n,negative_coefficients_checked:negative,constant_coefficients_checked:constant,retained_target_monomials:retained,nonzero_positive_remainder_coefficients:positive,nonzero_remainder_coefficients_by_degree:counts,map_ranks_over_rationals:ranks,maximum_absolute_map_entry:Math.max(...A.flat().map(Math.abs),...Y.flat().map(Math.abs),...Z.flat().map(Math.abs)),verifier_uses_only_standard_library:true,unbounded_family_constructed:false,external_mathematical_review:false,improves_omega:false};
 return{witness,report,equations};
}
const fs = require('node:fs');
const path = require('node:path');
const base = path.resolve(__dirname, '../../../results/canonical-moment-flags-2026-10-21');
for (const m of [5, 6, 7]) {
 const data = JSON.parse(fs.readFileSync(path.join(base, 'm'+m+'-integer-witness.json'), 'utf8'));
 const result = verifyBlocks(m, data.source[1], data.block_factors, data.block_moments);
 if (JSON.stringify(result.witness)!==JSON.stringify(data)) throw Error('map reconstruction differs');
 console.log(JSON.stringify({m, equations:result.equations, report:result.report}));
}
