from itertools import combinations

x = list(map(int, input().split()))

result = 0
# pair
for i, j in combinations(range(10), 2):
    result ^= x[i] | x[j] # 누적 XOR
# triplet
for i, j, k in combinations(range(10), 3):
    result ^= x[i] | x[j] | x[k]
print(result)
