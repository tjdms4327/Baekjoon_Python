import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bus = list(map(int, input().split()))
fee = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, m):
    s, e = bus[i-1], bus[i]
    total += fee[s-1][e-1]
print(total)