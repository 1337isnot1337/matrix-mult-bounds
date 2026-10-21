// Optional fast discovery implementation.  The Python companion replays
// the complete finite screen using only the standard library.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int n = 7;
std::array<int,n> ii, qq;
std::array<std::vector<int>,n> options;
std::array<std::vector<std::array<int,4>>,n> new_pairs;
std::array<std::uint64_t,n+1> completions;
std::uint64_t visited = 0, collision_pruned = 0, rank_pruned = 0, survivors = 0;
int shift, threshold = 11;
std::vector<std::array<int,n>> surviving_i;
std::vector<int> surviving_shifts, surviving_ranks;

void search(int depth, unsigned equal_i, unsigned equal_q, std::uint64_t exposed) {
    for (int value : options[depth]) {
        ++visited;
        ii[depth] = value;
        qq[depth] = value - shift - depth;
        unsigned next_i = equal_i, next_q = equal_q;
        for (int j=0;j<depth;++j) {
            if (ii[j] == ii[depth]) next_i |= 1u << (depth-j);
            if (qq[j] == qq[depth]) next_q |= 1u << (depth-j);
        }
        if (next_i & next_q) {
            collision_pruned += completions[depth+1];
            continue;
        }
        std::uint64_t next = exposed;
        for (const auto& point : new_pairs[depth]) {
            const auto [u,v,w,z] = point;
            int first = qq[w]+ii[z]-qq[v];
            int last = qq[u]+ii[v]-ii[w];
            if (0<=first && first<8 && 0<=last && last<8)
                next |= std::uint64_t{1} << (8*first+last);
        }
        int rank = __builtin_popcountll(next);
        if (rank > threshold) {
            rank_pruned += completions[depth+1];
            continue;
        }
        if (depth+1<n) search(depth+1,next_i,next_q,next);
        else {
            ++survivors;
            surviving_i.push_back(ii);
            surviving_shifts.push_back(shift);
            surviving_ranks.push_back(rank);
        }
    }
}

int main(int argc,char**argv) {
    if (argc>1) threshold=std::stoi(argv[1]);
    for (int u=0;u<n;++u) for (int v=0;v<n;++v)
        for (int w=0;w<n;++w) for (int z=0;z<n;++z)
            if (u+w==v+z)
                new_pairs[std::max({u,v,w,z})].push_back({u,v,w,z});
    std::uint64_t all = 0;
    for (shift=-7;shift<=1;++shift) {
        for (int v=0;v<n;++v) {
            options[v].clear();
            for (int i=0;i<8;++i) if (0<=i-shift-v && i-shift-v<8)
                options[v].push_back(i);
        }
        completions[n]=1;
        for (int v=n-1;v>=0;--v) completions[v]=completions[v+1]*options[v].size();
        all+=completions[0];
        search(0,0,0,0);
    }
    std::cout << "{\"threshold\":"<<threshold<<",\"complete_choices\":"<<all
              <<",\"visited_partial_choices\":"<<visited
              <<",\"injectivity_pruned_choices\":"<<collision_pruned
              <<",\"rank_pruned_choices\":"<<rank_pruned
              <<",\"survivors\":"<<survivors<<",\"surviving_choices\":[";
    for (std::size_t k=0;k<surviving_i.size();++k) {
        if(k)std::cout<<",";
        std::cout<<"{\"shift\":"<<surviving_shifts[k]<<",\"rank\":"<<surviving_ranks[k]<<",\"first_indices\":[";
        for(int j=0;j<n;++j)std::cout<<(j?",":"")<<surviving_i[k][j];
        std::cout<<"]}";
    }
    std::cout<<"]}\n";
    return all==collision_pruned+rank_pruned+survivors?0:2;
}
