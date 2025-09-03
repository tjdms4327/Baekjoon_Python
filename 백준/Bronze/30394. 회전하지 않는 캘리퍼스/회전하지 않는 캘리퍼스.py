import sys
input = sys.stdin.readline

n = int(input())
y = []
for _ in range(n):
    x, i = map(int, input().split())
    y.append(i)
print(max(y) - min(y))