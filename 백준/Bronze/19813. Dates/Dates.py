# bronzeIII_19813
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    if '.' in s:
        d, m, y = map(int, s.split('.'))
    else:
        m, d, y = map(int, s.split('/'))
    print(f'{d:02d}.{m:02d}.{y:04d} {m:02d}/{d:02d}/{y:04d}')