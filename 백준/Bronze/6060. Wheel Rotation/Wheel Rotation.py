import sys
input = sys.stdin.readline

n = int(input())
belt = {} # start, end, connect
for _ in range(n-1):
    s, d, c = map(int, input().split())
    belt[s] = [d, c]

start = 1
direction = 0
while start != n:
    d, c = belt[start]
    if c != 0:
        direction = (direction+1)%2

    start = d
print(direction)