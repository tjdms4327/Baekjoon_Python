import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    s=int(input())
    n=int(input())
    for _ in range(n):
        p,q=map(int, input().split())
        s+=(p*q)
    print(s)