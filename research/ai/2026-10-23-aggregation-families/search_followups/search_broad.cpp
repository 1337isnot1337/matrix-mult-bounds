#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
struct T {int p[3];};
struct S {vector<int> labels;};
int main(int argc,char**argv){
 if(argc<5){cerr<<"seed-file mode iterations rngseed [output]\n";return 2;}
 ifstream seedfile(argv[1]);int d,count;seedfile>>d>>count;int n=d/3,full=(1<<d)-1;
 string mode=argv[2];long long iterations=stoll(argv[3]);mt19937_64 rng(stoull(argv[4]));
 vector<int> masks;vector<int> ix(1<<d,-1);
 for(int b=0;b<=full;b++)if(__builtin_popcount((unsigned)b)==n){ix[b]=masks.size();masks.push_back(b);}
 int h=masks.size();vector<T> cand;vector<vector<int>> pairindex(h,vector<int>(h,-1));
 for(int i=0;i<h;i++)for(int j=0;j<h;j++)if(!(masks[i]&masks[j])){pairindex[i][j]=cand.size();cand.push_back({i,j,ix[full^masks[i]^masks[j]]});}
 vector<int> seed;
 for(int i=0;i<count;i++){int a,b,c;seedfile>>a>>b>>c;int t=pairindex[ix[a]][ix[b]];if(cand[t].p[2]!=ix[c])return 3;seed.push_back(t);}
 vector<vector<S>> survivors(h,vector<S>(h));
 for(int i=0;i<h;i++)for(int j=0;j<h;j++)for(int k=0;k<h;k++){
 int a=masks[i],b=masks[j],c=masks[k];bool bad;
 if(mode=="centered")bad=(((a&b&~c)|(a&c&~b)|(b&c&~a))==0);
 else bad=!(a&b)&&!(a&c)&&!(b&c);
 if(bad)survivors[i][j].labels.push_back(k);
 }
 vector<int> best=seed,cur;vector<vector<int>> pool{seed};
 vector<vector<int>> forbid(3,vector<int>(h));
 auto add=[&](int x){
 T a=cand[x];
 for(int y:cur){T b=cand[y];for(int k=0;k<3;k++){int r=(k+1)%3,s=(k+2)%3;for(int l:survivors[a.p[r]][b.p[s]].labels)forbid[k][l]++;for(int l:survivors[b.p[r]][a.p[s]].labels)forbid[k][l]++;}}
 for(int k=0;k<3;k++)forbid[k][a.p[k]]++;
 cur.push_back(x);
 };
 auto save=[&](){if(argc>5){ofstream f(argv[5]);f<<d<<" "<<best.size()<<"\n";for(int x:best)f<<masks[cand[x].p[0]]<<" "<<masks[cand[x].p[1]]<<" "<<masks[cand[x].p[2]]<<"\n";}};
 auto start=chrono::steady_clock::now();int maximal=0;vector<int> allowed;
 for(long long it=0;it<iterations;it++){
 cur.clear();for(auto&f:forbid)fill(f.begin(),f.end(),0);
 vector<int> base=pool[rng()%pool.size()];
 shuffle(base.begin(),base.end(),rng);
 size_t remove=(it%31==0)?base.size():1+(rng()%min((size_t)20,base.size()));
 for(size_t z=remove;z<base.size();z++)add(base[z]);
 while(true){allowed.clear();for(int x=0;x<(int)cand.size();x++){T a=cand[x];if(!forbid[0][a.p[0]]&&!forbid[1][a.p[1]]&&!forbid[2][a.p[2]])allowed.push_back(x);}if(allowed.empty())break;
 int chosen=allowed[rng()%allowed.size()];
 // Prefer low-damage insertions on half the restarts, with random tie-breaking.
 if(it%2==0&&allowed.size()>1){int bestscore=100000000;int tries=min(12,(int)allowed.size());for(int z=0;z<tries;z++){
 int x=allowed[rng()%allowed.size()];T a=cand[x];int score=0;array<vector<int>,3> fresh;for(int k=0;k<3;k++)fresh[k].push_back(a.p[k]);
 for(int y:cur){T b=cand[y];for(int k=0;k<3;k++){int r=(k+1)%3,s=(k+2)%3;for(int l:survivors[a.p[r]][b.p[s]].labels)if(!forbid[k][l])fresh[k].push_back(l);for(int l:survivors[b.p[r]][a.p[s]].labels)if(!forbid[k][l])fresh[k].push_back(l);}}
 for(auto&f:fresh){sort(f.begin(),f.end());f.erase(unique(f.begin(),f.end()),f.end());}
 for(int v:allowed){T b=cand[v];bool killed=false;for(int k=0;k<3;k++)if(binary_search(fresh[k].begin(),fresh[k].end(),b.p[k]))killed=true;score+=killed;}
 score=score*100+(int)(rng()%300);if(score<bestscore){bestscore=score;chosen=x;}
 }}add(chosen);
 }
 if(cur.size()>best.size()){best=cur;save();cerr<<"new best "<<best.size()<<" iteration "<<it<<" elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";pool.clear();}
 if(cur.size()+2>=best.size()) {if(pool.size()<512)pool.push_back(cur);else pool[rng()%pool.size()]=cur;}
 if(it%10000==0)cerr<<"iteration "<<it<<" best "<<best.size()<<" last "<<cur.size()<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 }
 save();cout<<"{\"mode\":\""<<mode<<"\",\"iterations\":"<<iterations<<",\"rng_seed\":"<<argv[4]<<",\"best\":"<<best.size()<<",\"elapsed_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
