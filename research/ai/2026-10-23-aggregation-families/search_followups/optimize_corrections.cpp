#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <vector>
using namespace std;
struct T{int p[3];};
int main(int argc,char**argv){if(argc<5)return 2;ifstream f(argv[1]);int d,p;f>>d>>p;int n=d/3,F=(1<<d)-1;vector<int>M;vector<int>I(1<<d,-1);for(int x=0;x<=F;x++)if(__builtin_popcount((unsigned)x)==n){I[x]=M.size();M.push_back(x);}int h=M.size();vector<T>C;vector<vector<int>>idx(h,vector<int>(h,-1));for(int a=0;a<h;a++)for(int b=0;b<h;b++)if(!(M[a]&M[b])){idx[a][b]=C.size();C.push_back({a,b,I[F^M[a]^M[b]]});}vector<int>seed;for(int i=0;i<p;i++){int a,b,c;f>>a>>b>>c;seed.push_back(idx[I[a]][I[b]]);}mt19937_64 rng(stoull(argv[3]));int iterations=stoi(argv[2]);vector<vector<int>>surv(h,vector<int>(h,-1));for(int a=0;a<h;a++)for(int b=0;b<h;b++)if(!(M[a]&M[b]))surv[a][b]=I[F^M[a]^M[b]];
 auto score=[&](const vector<int>&S){array<bool,4096>present{};for(int i:S)for(int j:S)for(int k:S){int a=M[C[i].p[0]],b=M[C[j].p[1]],c=M[C[k].p[2]];if(((a&b&~c)|(a&c&~b)|(b&c&~a))!=0)continue;int r=a&b&c;for(int s=r;s;s=(s-1)&r)present[s]=true;}array<int,5>counts{};for(int s=1;s<=F;s++)if(present[s])counts[__builtin_popcount((unsigned)s)]++;return counts;};
 auto key=[&](const array<int,5>&a){return a[1]*10000+a[2]*100+a[3];};
 vector<int>best=seed,cur;auto bestcounts=score(seed);vector<vector<int>>pool{seed};vector<array<int,5>>poolscore{bestcounts};auto start=chrono::steady_clock::now();
 for(int it=0;it<iterations;it++){cur.clear();array<vector<int>,3>bad;for(auto&b:bad)b.assign(h,0);auto add=[&](int x){T a=C[x];for(int y:cur){T b=C[y];for(int k=0;k<3;k++){int r=(k+1)%3,s=(k+2)%3;int z=surv[a.p[r]][b.p[s]];if(z>=0)bad[k][z]++;z=surv[b.p[r]][a.p[s]];if(z>=0)bad[k][z]++;}}for(int k=0;k<3;k++)bad[k][a.p[k]]++;cur.push_back(x);};
 vector<int>base=pool[rng()%pool.size()];shuffle(base.begin(),base.end(),rng);int remove=1+rng()%6;for(int z=remove;z<(int)base.size();z++)add(base[z]);vector<int>allow;
 while(true){allow.clear();for(int x=0;x<(int)C.size();x++){T a=C[x];if(!bad[0][a.p[0]]&&!bad[1][a.p[1]]&&!bad[2][a.p[2]])allow.push_back(x);}if(allow.empty())break;add(allow[rng()%allow.size()]);}
 if(cur.size()<best.size())continue;auto cs=score(cur);if(cur.size()>best.size()||key(cs)<key(bestcounts)){best=cur;bestcounts=cs;ofstream out(argv[4]);out<<d<<" "<<cur.size()<<"\n";for(int x:cur)out<<M[C[x].p[0]]<<" "<<M[C[x].p[1]]<<" "<<M[C[x].p[2]]<<"\n";cerr<<"best "<<cur.size()<<" correction "<<cs[1]<<","<<cs[2]<<","<<cs[3]<<" iteration "<<it<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";}
 if(cur.size()==best.size()&&key(cs)<=key(bestcounts)+3){if(pool.size()<256){pool.push_back(cur);poolscore.push_back(cs);}else {int at=rng()%pool.size();pool[at]=cur;poolscore[at]=cs;}}
 if(it%10000==0)cerr<<"iteration "<<it<<" best "<<best.size()<<" counts "<<bestcounts[1]<<","<<bestcounts[2]<<","<<bestcounts[3]<<"\n";
 }
 cout<<"best "<<best.size()<<" counts "<<bestcounts[1]<<","<<bestcounts[2]<<","<<bestcounts[3]<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
