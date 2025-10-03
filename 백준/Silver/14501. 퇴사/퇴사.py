# silverIII_14501
import sys
input = sys.stdin.readline

n = int(input())
D = [0] * (n+2)
T = [0] * (n+1)
P = [0] * (n+1)
for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())
    
for i in range(n, 0, -1):
    if i+T[i] > n+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], P[i] + D[i+T[i]])
print(D[1])