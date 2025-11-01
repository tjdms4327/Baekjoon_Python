# bronzeII_10420
import sys
input = sys.stdin.readline

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

n = int(input())

year, month, day = 2014, 4, 2
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(n - 1):
    if is_leap(year):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    
    day += 1
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

print(f"{year:04d}-{month:02d}-{day:02d}")