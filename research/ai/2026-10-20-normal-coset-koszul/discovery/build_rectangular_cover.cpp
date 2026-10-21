// Discovery only. The exported bytes are checked without this compiler.
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
using Pattern = std::array<int, 7>;

int main(int argc, char **argv) {
  if (argc != 2) return 2;
  std::vector<Pattern> patterns;
  for (int word = 0; word < 78125; ++word) {
    Pattern p{}; int t = word, sum = 0;
    for (int i = 0; i < 7; ++i) { p[i] = t % 5; t /= 5; sum += p[i]; }
    if (sum != 19) continue;
    bool canonical = true;
    for (int shift = 1; shift < 7; ++shift) {
      Pattern rotated{};
      for (int i = 0; i < 7; ++i) rotated[i] = p[(i + shift) % 7];
      if (rotated < p) { canonical = false; break; }
    }
    if (canonical) patterns.push_back(p);
  }
  std::sort(patterns.begin(), patterns.end());
  const int n = patterns.size();
  std::vector<std::vector<bool>> bad(n, std::vector<bool>(n));
  int edges = 0;
  for (int a = 0; a < n; ++a) for (int b = a + 1; b < n; ++b) {
    int best = 0;
    for (int shift = 0; shift < 7; ++shift) {
      int value = 0;
      for (int i = 0; i < 7; ++i) {
        int x = patterns[a][i], y = patterns[b][(i + shift) % 7];
        value += 3 * std::min(x,y) - (x == 1 && y == 1);
      }
      best = std::max(best,value);
    }
    if (best < 48) { bad[a][b] = bad[b][a] = true; ++edges; }
  }
  std::ofstream output(argv[1], std::ios::binary);
  if (!output) return 3;
  int triples = 0;
  for (int a = 0; a < n; ++a) for (int b = a + 1; b < n; ++b) {
    if (!bad[a][b]) continue;
    for (int c = b + 1; c < n; ++c) {
      if (!(bad[a][c] && bad[b][c])) continue;
      bool found = false;
      for (int j = 0; j < 7 && !found; ++j) for (int k = 0; k < 7 && !found; ++k) {
        int ranks[3] = {0,0,0};
        for (int i = 0; i < 7; ++i) {
          int x = patterns[a][i], y = patterns[b][(i+j)%7], z = patterns[c][(i+k)%7];
          ranks[0] += z * (3*std::min(x,y) - (x==1 && y==1));
          ranks[1] += y * (3*std::min(x,z) - (x==1 && z==1));
          ranks[2] += x * (3*std::min(y,z) - (y==1 && z==1));
        }
        for (int leg = 0; leg < 3; ++leg) if (ranks[leg] > 128) {
          unsigned char byte = (leg*7+j)*7+k;
          output.put(static_cast<char>(byte)); ++triples; found = true; break;
        }
      }
      if (!found) { std::cerr << "uncovered triple " << a << ',' << b << ',' << c << '\n'; return 4; }
    }
  }
  output.close();
  std::cout << "{\"classes\":" << n << ",\"bad_edges\":" << edges
            << ",\"explicit_triples\":" << triples << "}\n";
}
