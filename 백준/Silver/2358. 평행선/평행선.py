# silverIV_2358
import sys
input = sys.stdin.readline

X, Y = {}, {}

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    X[x] = X.get(x, 0) + 1
    Y[y] = Y.get(y, 0) + 1

count = 0
for val in X.values():
    if val >= 2:
        count += 1
for val in Y.values():
    if val >= 2:
        count += 1
print(count)