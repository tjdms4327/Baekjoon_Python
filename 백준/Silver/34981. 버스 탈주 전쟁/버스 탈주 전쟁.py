import sys
input = sys.stdin.readline

x, y = map(int, input().split())
start = 60*x + y

n = int(input())
cand = []

for _ in range(n):
    x, y, d = map(int, input().split())
    time = x*60 + y

    # 마지막 운행 시간
    last = time + ((1439 - time) // d) * d

    if start <= last:
        if start <= time:
            nxt = time
        else:
            diff = (start - time + d - 1) // d  # ceil
            nxt = time + diff * d
    else: # 다음 날 첫차
        nxt = time + 1440

    cand.append(nxt)

res = min(cand)
h, m = (res // 60) % 24, res % 60

print(f'{h:02d}:{m:02d}')