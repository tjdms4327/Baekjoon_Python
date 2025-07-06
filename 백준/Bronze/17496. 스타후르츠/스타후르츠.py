import sys
input=sys.stdin.readline

n,t,c,p=map(int, input().split())
tot=0
while n>t:
    tot+=c
    n-=t
print(tot*p)