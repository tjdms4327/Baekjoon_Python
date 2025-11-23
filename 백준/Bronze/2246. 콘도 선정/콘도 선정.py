import sys
input = sys.stdin.readline

n = int(input())
condo = []
for _ in range(n):
    d, c = map(int, input().split())
    condo.append([d, c])
condo.sort()

cost = 10001
ans = 0
for cand in condo:
    temp = cand[1]
    if temp < cost:
        cost = temp
        ans += 1
print(ans)