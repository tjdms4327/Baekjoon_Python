import sys
input = sys.stdin.readline

a, b = map(int, input().split())

result = 1
for i in range(a, b+1):
    result *= sum(range(1, i+1))
print(result % 14579)