import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())
print((3*n - m)*a + b if 3*n>m else 0)