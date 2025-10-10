# bronzeIII_13063
import sys
input = sys.stdin.readline
from math import ceil

while True:  
    n, m, k = map(int, input().split())
    if n == m == k == 0: break
    
    none = n - m - k
    needed = n//2 + 1 - m
    if needed <= 0:
        print(0)
    elif needed <= none:
        print(needed)
    else:
        print(-1)