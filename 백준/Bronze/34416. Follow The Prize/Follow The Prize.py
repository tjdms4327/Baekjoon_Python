# bronzeIII_34416
import sys
input = sys.stdin.readline

n = int(input()) # 컵 수
price = int(input()) # 상금 위치
cups = [0] * (n+1)
cups[price] = 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]
print(cups.index(1))