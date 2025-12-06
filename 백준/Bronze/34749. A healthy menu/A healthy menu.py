import sys
input = sys.stdin.readline

n,m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]

tot = 0
for g in zip(*G):
    tot += max(1, max(g))
print(tot)