# silverIV_14594
import sys
input = sys.stdin.readline

n = int(input())
rooms = [0] + [1]*n

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x, y):
        rooms[i] = 0
print(sum(rooms))
