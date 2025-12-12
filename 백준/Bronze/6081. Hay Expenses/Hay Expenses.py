import sys
input = sys.stdin.readline

n, q = map(int, input().split())
H = [int(input()) for _ in range(n)]

for _ in range(q):
    s, e = map(int, input().split())
    print(sum(H[s-1:e]))