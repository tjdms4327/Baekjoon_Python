# silverIV_32205
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

edges = set()
for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a in edges or b in edges or c in edges:
        print(1)
        sys.stdin.read()
        sys.exit()
    else:
        edges.update([a, b, c])
print(0) 