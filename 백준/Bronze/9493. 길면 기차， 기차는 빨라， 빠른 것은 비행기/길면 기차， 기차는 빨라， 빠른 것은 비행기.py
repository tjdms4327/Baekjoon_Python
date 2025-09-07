import sys
input = sys.stdin.readline

while True:
    m, a, b = map(int, input().split())
    if m == a == b == 0: 
        break

    time = round(abs(m/a*3600 - m/b*3600))
    h = time // 3600
    m_ = (time % 3600) // 60
    s = time % 60
    print(f'{h}:{m_:02d}:{s:02d}')
