import sys
input = sys.stdin.readline

n, f = map(int, input().split())

time = []
for _ in range(n):
    x, v = map(int, input().split())
    time.append((f-x)/v)

min_time = min(time)
print(time.index(min_time) + 1)