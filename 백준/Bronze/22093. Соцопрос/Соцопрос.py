# bronzeIII_22093.py
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n, a, b = map(int, input().split())
    print(max(0, a -b), min(a, n - b))