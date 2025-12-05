import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

time = 0
capacity = m
for a in A:
    if capacity < a:
        time += 1
        capacity = m
    print(time)
    capacity -= a