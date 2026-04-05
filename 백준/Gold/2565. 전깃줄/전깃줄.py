import sys
input = sys.stdin.readline

n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
lines = sorted(zip(A, B), key = lambda x:x[0])
B_sorted = [b for a, b in lines]
nb = len(B_sorted)

dp = [1] * nb
for i in range(nb):
    for j in range(i):
        if B_sorted[j] < B_sorted[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
max_line = max(dp)
print(nb - max_line)