# bronzeIII_14535
import sys
input = sys.stdin.readline

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
case = 0

while True:
    line = input()
    if not line:
        break
    n = int(line)
    if n == 0:
        break
    case += 1

    birth = {month: '' for month in months}
    for _ in range(n):
        d, m, y = map(int, input().split())
        # m이 1~12 범위인 경우만 처리
        if 1 <= m <= 12:
            birth[months[m-1]] += '*'

    print(f'Case #{case}:')
    for month in months:
        print(f'{month}:{birth[month]}')
