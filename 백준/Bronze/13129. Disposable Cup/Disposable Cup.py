import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

result = []
default = a * n
for i in range(1, n+1):
    default += b
    result.append(default)
print(*result)