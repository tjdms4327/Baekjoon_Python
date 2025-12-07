import sys
input = sys.stdin.readline

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0:
        break
    
    if y <= 0 or (m <= 0 or m > 12) or d <= 0:
        print('Invalid')
        continue
    
    days_in_month = [0, 31, 29 if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)) else 28,
                 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
    if d > days_in_month[m]:
        print('Invalid')
    else:
        print('Valid')