import sys
input = sys.stdin.readline

n, s = map(int, input().split())

velocity = 0
for _ in range(n):
    if velocity > s:
        velocity -= 1
    velocity += int(input())
print(velocity)
        