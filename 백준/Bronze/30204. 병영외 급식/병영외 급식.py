import sys
input = sys.stdin.readline

n, x = map(int, input().split())
P = list(map(int, input().split()))

if sum(P)%x==0:
    print(1)
else:
    print(0)