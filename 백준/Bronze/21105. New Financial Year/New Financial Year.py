# bronzeIII_21105.py
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p, c = map(float, input().split())
    o = p / (c/100 + 1)
    print(o)