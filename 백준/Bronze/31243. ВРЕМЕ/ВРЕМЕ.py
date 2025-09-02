import sys
input = sys.stdin.readline

times = []
for i in range(3):
    start_h, start_m, end_h, end_m = map(int, input().split())
    t = (end_h - start_h)*60 + (end_m - start_m)
    if end_h < start_h:
        t += 24*60
    times.append(t)
print(f'{min(times)//60}:{min(times)%60:02d}')
print(f'{max(times)//60}:{max(times)%60:02d}')