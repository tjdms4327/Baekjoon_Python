# bronzeIII_29720
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

min_q = n - m*k
max_q = n - (m*(k-1) + 1)
print(max(0, min_q), max(0, max_q))