import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = list(map(int, input().split())) + [0]*m

for i in range(n):
    share = list(map(int, input().split()))
    money[i] -= sum(share) # 남은 돈
    for j in range(n+m):
        money[j] += share[j]
print(*money)
