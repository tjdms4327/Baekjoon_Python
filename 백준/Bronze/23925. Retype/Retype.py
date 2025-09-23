# bronzeIII_23925.py
import sys
input = sys.stdin.readline

n = int(input())
for case in range(1, n+1):
    n, k, s = map(int, input().split())
    print(f'Case #{case}: {min(k-1 + 1 + n, k-s + n-s+1 + k-1)}')