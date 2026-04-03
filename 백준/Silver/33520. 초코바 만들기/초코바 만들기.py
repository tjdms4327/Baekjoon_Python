import sys
input = sys.stdin.readline

n = int(input())

w, h = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    
    w = max(w, min(a, b))
    h = max(h, max(a, b))

print(w * h)