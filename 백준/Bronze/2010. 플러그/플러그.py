import sys
input=sys.stdin.readline

n=int(input())
tot=0

for _ in range(n):
    tot+=int(input())
tot-=(n-1)
print(tot)