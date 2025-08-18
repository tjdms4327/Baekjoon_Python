import sys
input = sys.stdin.readline

n, x, k = map(int, input().strip().split())
balls = [0] * (n + 1)
balls[x] = 1 
for _ in range(k):
    a, b = map(int, input().strip().split())
    if balls[a] == 1:
        balls[b] = 1
        balls[a] = 0
    elif balls[b] == 1:
        balls[a] = 1
        balls[b] = 0
print(balls.index(1))
