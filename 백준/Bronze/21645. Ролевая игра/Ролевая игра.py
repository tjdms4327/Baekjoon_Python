# bronzeIII_21645.py
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
white, red = 0, 0
for i in range(1, m+1):
    red = max(red, i // k)
    white = max(white, i % k)
print(n * (white + red))