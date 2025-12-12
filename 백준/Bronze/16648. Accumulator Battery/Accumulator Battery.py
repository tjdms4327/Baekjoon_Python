import sys
input = sys.stdin.readline

t, p = map(int, input().split())

if p > 20:
    speed = (100-p)/t
    time = (p-20) / speed + (20/speed) * 2
else:
    speed = (40-2*p + 80) / t
    time = (p/speed) * 2
print(time)