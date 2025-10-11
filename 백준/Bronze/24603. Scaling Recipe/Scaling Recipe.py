# bronzeIII_24603
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
ingredients = [int(input()) for _ in range(n)]

for i in ingredients:
    print(int(i * y / x))