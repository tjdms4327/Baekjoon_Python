# bronzeI_11051
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
D = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(0, n+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1
for i in range(2, n+1):
    for j in range(1, i):
        D[i][j] = (D[i-1][j] + D[i-1][j-1]) % 10007
print(D[n][k])