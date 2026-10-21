// Discovery only. The Python verifier checks each exported tag independently.
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdint>
using P=std::array<int,7>;
std::vector<P> classes(int total){std::vector<P> out;for(int word=0;word<78125;++word){P p{};int t=word,s=0;for(int i=0;i<7;++i){p[i]=t%5;t/=5;s+=p[i];}if(s!=total)continue;bool canonical=true;for(int j=1;j<7;++j){P q{};for(int i=0;i<7;++i)q[i]=p[(i+j)%7];if(q<p){canonical=false;break;}}if(canonical)out.push_back(p);}std::sort(out.begin(),out.end());return out;}
int L,divisors[5],table[5][5][5];
int pair_tag(const P&a,const P&b,int third){for(int s=0;s<7;++s){int dot=0;for(int i=0;i<7;++i)dot+=a[i]*b[(i+s)%7];if(dot>64)return 1+s;}
for(int l=0;l<L;++l)for(int reverse=0;reverse<2;++reverse)for(int s=0;s<7;++s){int w=0;for(int i=0;i<7;++i){int x=a[i],y=b[(i+s)%7];w+=reverse?table[l][y][x]:table[l][x][y];}if(third*w>7*64*divisors[l])return 8+14*l+7*reverse+s;}return 0;}
int triple_tag(const P&a,const P&b,const P&c){P rows[3]={a,b,c};std::array<int,3> perm={0,1,2};int permutation=0;do{for(int l=0;l<L;++l)for(int j=0;j<7;++j)for(int k=0;k<7;++k){int rank=0;for(int i=0;i<7;++i)rank+=rows[perm[2]][(i+k)%7]*table[l][rows[perm[0]][i]][rows[perm[1]][(i+j)%7]];if(rank>64*divisors[l])return k+7*j+49*(permutation+6*l);}++permutation;}while(std::next_permutation(perm.begin(),perm.end()));return -1;}
int main(int argc,char**argv){if(argc!=4)return 2;std::ifstream tables(argv[1]),shapes(argv[2]);std::ofstream out(argv[3],std::ios::binary);tables>>L;if(L!=5)return 3;for(int l=0;l<L;++l){tables>>divisors[l];for(int a=0;a<5;++a)for(int b=0;b<5;++b)tables>>table[l][a][b];}if(!tables||!out)return 4;int a,b,c;while(shapes>>a>>b>>c){auto A=classes(a),B=classes(b),C=classes(c);std::vector<std::vector<char>> ab(A.size(),std::vector<char>(B.size())),ac(A.size(),std::vector<char>(C.size())),bc(B.size(),std::vector<char>(C.size()));long long nab=0,nac=0,nbc=0,nt=0;auto grid=[&](const std::vector<P>&X,const std::vector<P>&Y,int third,std::vector<std::vector<char>>&bad,long long&n){for(int i=0;i<(int)X.size();++i)for(int j=0;j<(int)Y.size();++j){int t=pair_tag(X[i],Y[j],third);out.put(char(t));if(!t){bad[i][j]=1;++n;}}};grid(A,B,c,ab,nab);grid(A,C,b,ac,nac);grid(B,C,a,bc,nbc);for(int i=0;i<(int)A.size();++i)for(int j=0;j<(int)B.size();++j)if(ab[i][j])for(int k=0;k<(int)C.size();++k)if(ac[i][k]&&bc[j][k]){int tag=triple_tag(A[i],B[j],C[k]);if(tag<0){std::cerr<<"unexcluded triangle "<<a<<","<<b<<","<<c<<"\n";return 5;}out.put(char(tag&255));out.put(char(tag>>8));++nt;}
std::cout<<"{\"shape\":["<<a<<","<<b<<","<<c<<"],\"classes\":["<<A.size()<<","<<B.size()<<","<<C.size()<<"],\"uncertified_pairs\":["<<nab<<","<<nac<<","<<nbc<<"],\"explicit_triangles\":"<<nt<<"}\n";}
return out?0:6;}
