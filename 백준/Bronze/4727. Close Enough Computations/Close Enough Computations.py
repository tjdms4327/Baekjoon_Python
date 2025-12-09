import sys
input = sys.stdin.readline

while True:
    cal, f, c, p = map(int, input().split())
    if cal==f==c==p==0:
        break
    
    min_cal = 9*(max(0,f-0.5)) + 4*(max(0,c-0.5)) + 4*(max(0,p-0.5))
    over_cal = 9*(f+0.5) + 4*(c+0.5) + 4*(p+0.5)
    if min_cal <= cal < over_cal:
        print('yes')
    else:
        print('no')