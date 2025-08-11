import sys
input=sys.stdin.readline

a, b, c, d=map(int, input().split())
x=[1, 2, 3]
ans=[]
for i in x:
    if a**i+b**i+c**i==d:
        ans.append(i)

if len(ans)==1: print(*ans)
else: print(-1)