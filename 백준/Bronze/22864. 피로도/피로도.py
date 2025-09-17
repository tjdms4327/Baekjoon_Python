import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())

work = 0
fatigue = 0
for _ in range(24):
    if fatigue + a <= m:
        fatigue += a
        work += b
    else:
        fatigue -= c
    
    if fatigue < 0:
        fatigue = 0
print(work)