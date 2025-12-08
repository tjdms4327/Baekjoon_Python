import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
snake = {}
for _ in range(b):
    x, y = map(int, input().split())
    snake[x] = y
dice = [int(input()) for _ in range(c)]

positions = [1]*a
idx = 0
for x in dice:
    positions[idx] += x
    
    if positions[idx] >= 100:
        positions[idx] = 100
        break
    if positions[idx] in snake:
        positions[idx] = snake[positions[idx]]
    if positions[idx] == 100:
        break
    
    idx = (idx+1)%a

for n, p in enumerate(positions, start=1):
    print(f'Position of player {n} is {p}.')