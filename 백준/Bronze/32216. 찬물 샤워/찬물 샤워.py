import sys
input = sys.stdin.readline

n, k, t = map(int, input().split())
D = list(map(int, input().split()))

unpleasant = 0
for di in D:
    if t > k:
        t = t + di - abs(t - k)
    elif t < k:
        t = t + di + abs(t - k)
    else:
        t += di
    unpleasant += abs(t - k)
print(unpleasant)