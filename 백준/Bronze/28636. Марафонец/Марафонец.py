# bronzeIII_28636
import sys
input = sys.stdin.readline

n = int(input())
time = 0
for _ in range(n):
    m, s = map(int, input().split(':'))
    time += 60 * m + s
h, res = divmod(time, 3600)
m, s = divmod(res, 60)
print(f'{h:02d}:{m:02d}:{s:02d}')