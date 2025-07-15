tot=0

n=int(input())
for _ in range(n):
    q, y=map(float, input().split())
    tot+=(q*y)
print(tot)