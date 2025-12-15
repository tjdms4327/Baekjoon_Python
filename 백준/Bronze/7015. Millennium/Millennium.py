import sys
input = sys.stdin.readline

def days_until(y, m, d):
    days = d-1
    for year in range(1, y):
        if year % 3 == 0:
            days += 200
        else:
            days += 195  
    for month in range(1, m):
        if y % 3 == 0:
            days += 20
        else:
            if month % 2 == 1:
                days += 20
            else:
                days += 19 
    return days

n = int(input())

target = days_until(1000, 1, 1)
for _ in range(n):
    y, m, d = map(int, input().split())
    birth = days_until(y, m, d)
    print(target - birth)
    