# bronzeIII_11176
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    e, n = map(int, input().split())
    do = [int(input()) for _ in range(n)]

    print(sum(1 for i in range(n) if do[i] > e))