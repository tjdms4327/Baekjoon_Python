# bronzeII_21918
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lights = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        i, x = b, c
        lights[i] = x
    elif a == 2:
        l, r = b, c
        for i in range(l, r+1):
            lights[i] = (lights[i] + 1) % 2
    elif a == 3:
        l, r = b, c
        lights = lights[:l] + [0] * (r - l + 1) + lights[r+1:]
    else:
        l, r = b, c
        lights = lights[:l] + [1] * (r - l + 1) + lights[r+1:]

print(*lights[1:])