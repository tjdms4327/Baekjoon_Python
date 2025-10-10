# bronzeIII_9848
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
T = [int(input()) for _ in range(n)]

gift = 0
for i in range(1, n):
    if T[i-1] - k >= T[i]:
        gift += 1
print(gift)