import sys
input = sys.stdin.readline

a, b = map(int, input().split())
while a!= b:
    a, b = max(a, b) - min(a, b), min(a, b)
print(b)