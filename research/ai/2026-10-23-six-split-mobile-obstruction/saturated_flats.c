#include <stdio.h>
#include <stdlib.h>

/* Exhaustive saturation and mobile-span checks on original 0,+1,-1 rows.
   F_101 determines the fixed flats. F_1009 computes the ranks of at
   most six original rows; the bounded-minor proof is in README.md. */
#define N 47
#define D 20
#define P 101
#define Q 1009
#define FOUR_SUBSETS 178365
static int original[N][D], reduced[N][D], weight[N], mobile[4][D];
static int inv_p[P], inv_q[Q];
typedef struct { unsigned long long mask; unsigned hits; } Flat;

static int mod(int value, int prime) {
    value %= prime;
    return value < 0 ? value + prime : value;
}

static int compare_flats(const void *left, const void *right) {
    unsigned long long a = ((const Flat *)left)->mask;
    unsigned long long b = ((const Flat *)right)->mask;
    return (a > b) - (a < b);
}

static int rank_q(int rows[6][D], int count) {
    int rank = 0;
    for (int col = 0; col < D && rank < count; col++) {
        int found = rank;
        while (found < count && rows[found][col] == 0) found++;
        if (found == count) continue;
        for (int j = 0; j < D; j++) {
            int swap = rows[rank][j];
            rows[rank][j] = rows[found][j];
            rows[found][j] = swap;
        }
        int scale = inv_q[rows[rank][col]];
        for (int j = col; j < D; j++) rows[rank][j] = rows[rank][j] * scale % Q;
        for (int i = rank + 1; i < count; i++) {
            int factor = rows[i][col];
            for (int j = col; j < D; j++)
                rows[i][j] = mod(rows[i][j] - factor * rows[rank][j], Q);
        }
        rank++;
    }
    return rank;
}

int main(int argc, char **argv) {
    if (argc != 2) return 2;
    FILE *input = fopen(argv[1], "r");
    if (!input) return 3;
    for (int i = 0; i < N; i++) {
        if (fscanf(input, "%d", &weight[i]) != 1 || weight[i] < 0 || weight[i] > 4) return 4;
        for (int j = 0; j < D; j++) {
            if (fscanf(input, "%d", &original[i][j]) != 1 || original[i][j] < -1 || original[i][j] > 1) return 4;
            reduced[i][j] = mod(original[i][j], P);
        }
    }
    for (int i = 0; i < 4; i++) for (int j = 0; j < D; j++)
        if (fscanf(input, "%d", &mobile[i][j]) != 1 || mobile[i][j] < -1 || mobile[i][j] > 1) return 4;
    char extra;
    if (fscanf(input, " %c", &extra) == 1) return 4;
    fclose(input);
    for (int i = 1; i < P; i++) for (int j = 1; j < P; j++)
        if (i * j % P == 1) inv_p[i] = j;
    for (int i = 1; i < Q; i++) for (int j = 1; j < Q; j++)
        if (i * j % Q == 1) inv_q[i] = j;

    Flat *flats = malloc(FOUR_SUBSETS * sizeof(*flats));
    if (!flats) return 5;
    unsigned long all = 0, independent = 0, saturated = 0;
    unsigned long weight_histogram[4 * N + 1] = {0};
    unsigned long rank_counts[2][7][7] = {{{0}}};
    unsigned long failures[2] = {0}, unique_hits[2] = {0};
    int witnesses[2][4] = {{-1, -1, -1, -1}, {-1, -1, -1, -1}};
    int maximum_weight = 0;
    for (int a = 0; a < N; a++) for (int b = a + 1; b < N; b++)
    for (int c = b + 1; c < N; c++) for (int d = c + 1; d < N; d++) {
        all++;
        int ids[4] = {a, b, c, d}, basis[4][D], pivots[4], rank = 0;
        for (int i = 0; i < 4; i++) for (int j = 0; j < D; j++) basis[i][j] = reduced[ids[i]][j];
        for (int col = 0; col < D && rank < 4; col++) {
            int found = rank;
            while (found < 4 && basis[found][col] == 0) found++;
            if (found == 4) continue;
            for (int j = 0; j < D; j++) {
                int swap = basis[rank][j]; basis[rank][j] = basis[found][j]; basis[found][j] = swap;
            }
            int scale = inv_p[basis[rank][col]];
            for (int j = col; j < D; j++) basis[rank][j] = basis[rank][j] * scale % P;
            for (int i = 0; i < 4; i++) if (i != rank) {
                int factor = basis[i][col];
                for (int j = col; j < D; j++) basis[i][j] = mod(basis[i][j] - factor * basis[rank][j], P);
            }
            pivots[rank++] = col;
        }
        if (rank < 4) continue;
        independent++;
        int total = 0;
        unsigned long long mask = 0;
        for (int i = 0; i < N; i++) {
            int contained = 1;
            for (int col = 0; col < D; col++) {
                int value = 0;
                for (int j = 0; j < 4; j++) value += reduced[i][pivots[j]] * basis[j][col];
                if (value % P != reduced[i][col]) { contained = 0; break; }
            }
            if (contained) { total += weight[i]; mask |= 1ULL << i; }
        }
        weight_histogram[total]++;
        if (total > maximum_weight) maximum_weight = total;
        if (total != 16) continue;
        Flat entry = {mask, 0};
        for (int pair = 0; pair < 2; pair++) {
            int plus_x[6][D] = {{0}}, plus_xy[6][D] = {{0}};
            for (int i = 0; i < 4; i++) for (int j = 0; j < D; j++)
                plus_x[i][j] = plus_xy[i][j] = mod(original[ids[i]][j], Q);
            for (int j = 0; j < D; j++) {
                plus_x[4][j] = plus_xy[4][j] = mod(mobile[2 * pair][j], Q);
                plus_xy[5][j] = mod(mobile[2 * pair + 1][j], Q);
            }
            int with_x = rank_q(plus_x, 5), with_xy = rank_q(plus_xy, 6);
            rank_counts[pair][with_x][with_xy]++;
            if (with_xy != with_x + 1) failures[pair]++;
            if (with_x == 4) {
                entry.hits |= 1U << pair;
                if (witnesses[pair][0] < 0)
                    for (int i = 0; i < 4; i++) witnesses[pair][i] = ids[i];
            }
        }
        flats[saturated++] = entry;
    }
    qsort(flats, saturated, sizeof(*flats), compare_flats);
    unsigned long unique = 0;
    for (unsigned long i = 0; i < saturated; i++) {
        if (i && flats[i].mask == flats[i - 1].mask) {
            if (flats[i].hits != flats[i - 1].hits) return 6;
            continue;
        }
        unique++;
        for (int pair = 0; pair < 2; pair++) unique_hits[pair] += (flats[i].hits >> pair) & 1U;
    }
    free(flats);
    printf("{\"fixed_prime\":%d,\"intersection_prime\":%d,\"fixed_vectors\":%d,\"dimension\":%d,", P, Q, N, D);
    printf("\"four_subsets\":%lu,\"independent_four_subsets\":%lu,\"maximum_fixed_weight\":%d,", all, independent, maximum_weight);
    printf("\"saturated_basis_count\":%lu,\"unique_saturated_flats\":%lu,\"fixed_weight_histogram\":{", saturated, unique);
    int first = 1;
    for (int i = 0; i <= 4 * N; i++) if (weight_histogram[i]) {
        printf("%s\"%d\":%lu", first ? "" : ",", i, weight_histogram[i]); first = 0;
    }
    printf("},\"mobile_pairs\":[");
    for (int pair = 0; pair < 2; pair++) {
        printf("%s{\"rank_increment_failures\":%lu,\"unique_nonzero_intersections\":%lu,\"allowed_line_witness_basis\":[",
               pair ? "," : "", failures[pair], unique_hits[pair]);
        for (int i = 0; i < 4; i++) printf("%s%d", i ? "," : "", witnesses[pair][i]);
        printf("],\"rank_pair_histogram\":[");
        first = 1;
        for (int x = 0; x <= 6; x++) for (int xy = 0; xy <= 6; xy++) if (rank_counts[pair][x][xy]) {
            printf("%s[%d,%d,%lu]", first ? "" : ",", x, xy, rank_counts[pair][x][xy]); first = 0;
        }
        printf("]}");
    }
    printf("]}\n");
    return 0;
}
