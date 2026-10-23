#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
struct Stair {vector<int> f; int64_t cost;};
int64_t choose(int n,int k){int64_t c=1;for(int i=1;i<=k;i++)c=c*(n-i+1)/i;return c;}
int main(){
 for(int j=0;j<=3;j++){
  int D=6*j,k=6-j;int64_t scale=1;for(int i=j;i<3;i++)scale*=16;
  vector<int64_t> p(1,1);int q[]={17,9,9,18,9,9,17};
  for(int t=0;t<j;t++){vector<int64_t> b(p.size()+6);for(size_t a=0;a<p.size();a++)for(int d=0;d<7;d++)b[a+d]+=p[a]*q[d];p=b;}
  vector<int64_t> pref(D+2,0),counts(k+1);for(int i=0;i<=D;i++)pref[i+1]=pref[i]+p[i];for(int e=0;e<=k;e++)counts[e]=scale*choose(k,e);
  vector<Stair> fs;vector<int> f(k+1);
  function<void(int,int)> rec=[&](int e,int top){if(e==k+1){int64_t cost=0;for(int x=0;x<=k;x++)cost+=counts[x]*pref[f[x]+1];fs.push_back({f,cost});return;}for(int v=-1;v<=top;v++){f[e]=v;rec(e+1,v);}};rec(0,D);
  sort(fs.begin(),fs.end(),[](const Stair&a,const Stair&b){return a.cost<b.cost||(a.cost==b.cost&&a.f<b.f);});
  int64_t best=scale*pref.back()*(int64_t(1)<<k),tested=0;array<vector<int>,3> witness;
  for(size_t a=0;a<fs.size();a++){
   if(2*fs[a].cost>=best)break;
   for(size_t b=a;b<fs.size();b++){
    int64_t cost=fs[a].cost+fs[b].cost;if(cost>=best)break;tested++;
    vector<int> mp(k+1,1000),g(k+1);
    for(int u=0;u<=k;u++)if(fs[a].f[u]<D)for(int v=0;v<=k-u;v++)if(fs[b].f[v]<D)mp[u+v]=min(mp[u+v],fs[a].f[u]+fs[b].f[v]);
    for(int t=1;t<=k;t++)mp[t]=min(mp[t],mp[t-1]);
    for(int c=0;c<=k;c++){g[c]=max(-1,D-2-mp[k-c]);cost+=counts[c]*pref[g[c]+1];}
    if(cost<best){best=cost;witness={fs[a].f,fs[b].f,g};}
   }
  }
  cout<<"j "<<j<<" staircases "<<fs.size()<<" evaluated_pairs "<<tested<<" cost "<<best<<"\n";
  for(auto&v:witness){for(int x:v)cout<<x<<" ";cout<<"\n";}cout.flush();
 }
}
