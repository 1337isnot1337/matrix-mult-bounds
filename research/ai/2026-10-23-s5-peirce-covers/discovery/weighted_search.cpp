#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
vector<int64_t> mul(const vector<int64_t>&a,const vector<int64_t>&b){vector<int64_t> c(a.size()+b.size()-1);for(size_t i=0;i<a.size();i++)if(a[i])for(size_t j=0;j<b.size();j++)if(b[j])c[i+j]+=a[i]*b[j];return c;}
int main(int argc,char**argv){
 const int r=argc>1?stoi(argv[1]):1;
 const int counts[19]={1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,16,16,16};
 const vector<array<int,3>> support={{0,7,7},{1,6,7},{2,5,7},{2,7,7},{2,11,15},{3,3,7},{3,4,7},{3,5,6},{3,5,7},{3,7,7},{3,11,14},{4,5,6},{4,6,7},{4,7,7},{4,10,15},{4,11,14},{4,11,15},{5,5,6},{5,5,7},{5,6,7},{5,7,7},{5,10,14},{5,11,14},{5,11,15},{6,7,7},{6,9,15},{6,10,15},{6,11,13},{6,11,15},{7,7,7},{7,8,15},{7,9,14},{7,10,13},{7,10,14},{7,10,15},{7,11,12},{7,11,14},{7,11,15},{8,15,18},{9,14,18},{10,13,18},{10,14,18},{10,15,17},{10,15,18},{11,12,18},{11,14,17},{11,14,18},{11,15,18},{16,18,18},{17,17,18},{17,18,18},{18,18,18}};
 const vector<int> c1={6,7,10,11,18},c2={6,7,14,15,18};
 for(int j=0;j<=3;j++){
  int k=3*(r+1)-j;int64_t scale=1;for(int t=j;t<3;t++)scale*=16;
  int64_t best=INT64_MAX;array<int,7> witness{};int cases=0;
  for(int u=1;u<=3;u++)for(int v=-u;v<=u;v++)for(int t1=0;t1<=4;t1++)for(int t2=t1;t2<=4;t2++)for(int h=1;h<=24;h++){
   vector<int>d={12*u,10*u+2*v,8*u-2*v,6*u,6*u,4*u+2*v,2*u-2*v,0,10*u-v,8*u+v,4*u-v,2*u+v,10*u-v,8*u+v,4*u-v,2*u+v,12*u,6*u,0};
   for(int i=0;i<19;i++){if(find(c1.begin(),c1.end(),i)==c1.end())d[i]+=t1;if(find(c2.begin(),c2.end(),i)==c2.end())d[i]+=t2;}
   int D=0;for(auto&e:support)D=max(D,d[e[0]]+d[e[1]]+d[e[2]]);
   vector<int64_t>P(*max_element(d.begin(),d.end())+1);for(int i=0;i<19;i++)P[d[i]]+=counts[i];
   vector<int64_t>C(h+1);C[0]=C[h]=1;vector<int64_t>poly(1,1);
   for(int t=0;t<j;t++)poly=mul(poly,P);for(int t=0;t<k;t++)poly=mul(poly,C);
   int limit=int(poly.size())-1,budget=j*D+k*h;vector<int64_t>pref(poly.size()+1);vector<int>ends;
   for(int t=0;t<=limit;t++){pref[t+1]=pref[t]+poly[t];if(poly[t])ends.push_back(t-1);}ends.push_back(limit);
   int64_t cost=pref.back();array<int,3>cuts={limit,-1,-1};
   for(int a:ends)for(int b:ends){int c=budget-2-a-b;if(c < -1)continue;int64_t value=pref[a+1]+pref[b+1]+pref[min(c+1,limit+1)];if(value<cost){cost=value;cuts={a,b,c};}}
   cases++;cost*=scale;
   if(cost<best){best=cost;witness={u,v,t1,t2,h,cuts[0],cuts[1]};cout<<"best "<<j<<" "<<best<<" u "<<u<<" v "<<v<<" q1 "<<t1<<" q2 "<<t2<<" h "<<h<<" D "<<D<<" cuts "<<cuts[0]<<" "<<cuts[1]<<" "<<cuts[2]<<"\n";cout.flush();}
  }
  cout<<"FINAL "<<j<<" "<<best<<" cases "<<cases<<"\n";cout.flush();
 }
}
