import sys
input = sys.stdin.readline

n = int(input())
x, _, r = map(int, input().split())
lines = [int(input()) for _ in range(n)]

min_x, max_x = x-r, x+r
inside = border = 0
for t in lines:
    if t==min_x or t==max_x:
        border += 1
    elif min_x < t < max_x:
        inside += 1
print(inside, border)