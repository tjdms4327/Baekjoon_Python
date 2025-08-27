import sys
input = sys.stdin.readline

n, c = map(int, input().split())
total_seconds = 0
for _ in range(n):
    m, s = input().split(":")
    total_seconds += int(m) * 60 + int(s)
    
total_seconds -= (n - 1) * c

hh = total_seconds // 3600
mm = (total_seconds % 3600) // 60
ss = total_seconds % 60

print(f"{hh:02d}:{mm:02d}:{ss:02d}")