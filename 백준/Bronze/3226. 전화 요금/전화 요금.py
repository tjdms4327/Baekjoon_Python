# bronzeI_3266
import sys
input = sys.stdin.readline

pay = 0

n = int(input())
for _ in range(n):
    time, d = input().strip().split()
    h, m = map(int, time.split(':'))
    d = int(d)
    
    for _ in range(d):
        m += 1
        if m >= 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        
        if 7*60 < 60*h+m <= 19*60:
            pay += 10
        else:
            pay += 5
print(pay)