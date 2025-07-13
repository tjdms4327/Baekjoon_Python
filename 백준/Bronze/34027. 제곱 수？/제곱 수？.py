import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    temp=n**(1/2)
    if int(temp)**2==n: print(1)
    else: print(0)