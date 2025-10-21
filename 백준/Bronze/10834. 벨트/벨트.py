# bronzeII_10834
import sys
input = sys.stdin.readline

direction = -1
temp = 1
m = int(input())
for _ in range(m):
    a, b, belt = map(int, input().split())
    
    if direction == -1:
        direction = belt
    else:
        if belt == 1:
            direction = (direction + 1) % 2
    
    property = b/a
    temp *= property

print(direction, int(temp))