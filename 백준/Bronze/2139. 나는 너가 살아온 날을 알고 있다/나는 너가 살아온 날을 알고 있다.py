# bronzeII_2139
import sys
input = sys.stdin.readline

def count_date(y, m, d):
    leap = (True if (y%4==0 and y%100!=0) or (y%400==0) else False)
    
    date = d
    for i in range(1, m):
        if i == 2:
            if leap:
                date += 29
            else:
                date += 28
        elif i in [4, 6, 9, 11]:
            date += 30
        else:
            date += 31
    return date

while True:  
    d, m, y = map(int, input().split())
    if d == m == y == 0: break
    
    print(count_date(y, m, d))
    