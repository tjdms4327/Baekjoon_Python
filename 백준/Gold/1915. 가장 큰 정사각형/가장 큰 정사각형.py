# goldIV_1915
import sys
input = sys.stdin.readline

D = [[0 for j in range(1001)] for i in range(1001)]
n, m = map(int, input().split())
max = 0
for i in range(n):
    numbers = list(input())
    for j in range(m):
        D[i][j] = int(numbers[j])
        if D[i][j] == 1 and j>0 and i>0:
            D[i][j] = min(D[i-1][j-1], D[i-1][j], D[i][j-1]) + D[i][j]
        if max < D[i][j]:
            max = D[i][j]
print(max**2)