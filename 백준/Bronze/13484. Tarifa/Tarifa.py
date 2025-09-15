import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
total = sum([int(input()) for _ in range(n)])
print((n + 1) * x - total)