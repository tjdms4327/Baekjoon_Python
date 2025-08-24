import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())   # 예: 0 1 0 입력
seconds = h*3600 + m*60 + s

q = int(input())
for _ in range(q):
    s = input().strip()
    if s == '3':
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        print(f'{h} {m} {s}')
    else:
        n, t_second = map(int, s.split())
        if n == 1:
            seconds += t_second
        elif n == 2:
            seconds -= t_second
    seconds %= 24*3600 # 하루 넘어가면 순환
