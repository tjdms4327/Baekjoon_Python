# bronzeII_2391.py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = int(input())
    diff, word = float('inf'), ''
    for i in range(n):
        w = input().strip()
        diff_count = sum(a != b for a, b in zip(s, w))
        if diff > diff_count:
            diff = diff_count
            word = w
    print(word)