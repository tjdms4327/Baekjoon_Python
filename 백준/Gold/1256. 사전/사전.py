# goldII_1256
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
D = [[0 for j in range(202)] for i in range(202)]
for i in range(201):
    for j in range(i+1):
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j]
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001

if D[n+m][m] < k:
    print(-1)
else:
    while not (n==0 and m==0):
        if D[n-1+m][m] >= k:
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= D[n-1+m][m]
            m -= 1