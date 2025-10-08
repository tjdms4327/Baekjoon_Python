# bronzeIII_24333
import sys
input = sys.stdin.readline

l1, r1, l2, r2, k = map(int, input().split())

start, end = max(l1, l2), min(r1, r2)
time = end - start + 1
if start <= k <= end:
    time -= 1
print(max(0, time))