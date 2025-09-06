import sys
input = sys.stdin.readline

times = []
for _ in range(int(input())):
    t, m = map(int, input().split())
    if m == 1:
        times.append(t)

gap = []
for i in range(0, len(times)-1):
    gap.append(times[i+1] - times[i])
print(max(gap))