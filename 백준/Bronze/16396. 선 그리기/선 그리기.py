import sys
input = sys.stdin.readline

n = int(input())
lines = set()
for _ in range(n):
    x, y = map(int, input().split())
    
    lines.update(range(x, y))
print(len(lines))