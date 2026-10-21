#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Exhaustive finite-field screen of the retained external 76 vectors.
   No floating arithmetic is used in membership or acceptance. */
#define N 76
#define D 20
#define P 101
static int x[N][D], inv[P];
static int mod(int a) { a %= P; return a < 0 ? a+P : a; }
int main(int argc, char **argv) {
  if(argc != 2) return 2;
  FILE *f = fopen(argv[1], "r");
  if(!f) return 3;
  for(int i=0;i<N;i++) for(int j=0;j<D;j++) {
    if(fscanf(f,"%d", &x[i][j])!=1) return 4;
    x[i][j]=mod(x[i][j]);
  }
  fclose(f);
  for(int i=1;i<P;i++) for(int j=1;j<P;j++)
    if(i*j%P==1) inv[i]=j;
  unsigned long all=0, independent=0, histogram[N+1]={0};
  int best=0, best_basis[4]={0}, best_inside[N]={0};
  for(int a=0;a<N;a++) for(int b=a+1;b<N;b++)
  for(int c=b+1;c<N;c++) for(int d=c+1;d<N;d++) {
    all++;
    int ids[4]={a,b,c,d}, basis[4][D], piv[4], rank=0;
    for(int i=0;i<4;i++) for(int j=0;j<D;j++) basis[i][j]=x[ids[i]][j];
    for(int j=0;j<D && rank<4;j++) {
      int k=rank;
      while(k<4 && basis[k][j]==0) k++;
      if(k==4) continue;
      if(k!=rank) for(int col=0;col<D;col++) {
        int tmp=basis[k][col]; basis[k][col]=basis[rank][col]; basis[rank][col]=tmp;
      }
      int scale=inv[basis[rank][j]];
      for(int col=j;col<D;col++) basis[rank][col]=basis[rank][col]*scale%P;
      for(int i=0;i<4;i++) if(i!=rank && basis[i][j]) {
        int factor=basis[i][j];
        for(int col=j;col<D;col++) basis[i][col]=mod(basis[i][col]-factor*basis[rank][col]);
      }
      piv[rank++]=j;
    }
    if(rank<4) continue;
    independent++;
    int inside[N], count=0, nonpiv[D], ncols=0;
    for(int j=0;j<D;j++) {
      int is_pivot=0;
      for(int k=0;k<4;k++) if(piv[k]==j) is_pivot=1;
      if(!is_pivot) nonpiv[ncols++]=j;
    }
    for(int i=0;i<N;i++) {
      int coeff[4];
      for(int k=0;k<4;k++) coeff[k]=x[i][piv[k]];
      int yes=1;
      for(int col=0;col<ncols;col++) {
        int j=nonpiv[col], z=0;
        for(int k=0;k<4;k++) z += coeff[k]*basis[k][j];
        if(z%P != x[i][j]) { yes=0; break; }
      }
      if(yes) inside[count++]=i;
    }
    histogram[count]++;
    if(count>best) {
      best=count;
      for(int i=0;i<4;i++) best_basis[i]=ids[i];
      for(int i=0;i<count;i++) best_inside[i]=inside[i];
    }
  }
  printf("{\"prime\":%d,\"vectors\":%d,\"dimension\":%d,\"four_subsets\":%lu,\"independent_four_subsets\":%lu,\"maximum_flat_cardinality\":%d,\"witness_basis\":[",P,N,D,all,independent,best);
  for(int i=0;i<4;i++) printf("%s%d",i?",":"",best_basis[i]);
  printf("],\"witness_members\":[");
  for(int i=0;i<best;i++) printf("%s%d",i?",":"",best_inside[i]);
  printf("],\"basis_weighted_histogram\":{");
  int first=1;
  for(int i=0;i<=N;i++) if(histogram[i]) {
    printf("%s\"%d\":%lu",first?"":",",i,histogram[i]);first=0;
  }
  printf("}}\n");
  return 0;
}
