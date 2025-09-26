# bronzeII_6993
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w, n = input().strip().split()
    n = int(n)
      
    print(f'Shifting {w} by {n} positions gives us: {w[(-1)*n:] + w[:(-1)*n]}')