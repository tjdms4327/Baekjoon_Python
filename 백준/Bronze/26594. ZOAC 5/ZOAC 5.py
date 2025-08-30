import sys
input = sys.stdin.readline

s = input().strip()
n = len(s) // len(set(s))
print(n)