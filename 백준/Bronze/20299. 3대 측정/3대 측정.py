# bronzeII_20299
import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
result = []
for _ in range(n):
    X = list(map(int, input().split()))
    if all(x>=l for x in X) and (sum(X) >= k):
        result.extend(X)

print(len(result) // 3)
print(*result)