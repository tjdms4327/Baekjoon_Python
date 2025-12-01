import sys
input = sys.stdin.readline

h, m, s = map(int, input().split(':'))
now = s + 60*m + 3600*h
h, m, s = map(int, input().split(':'))
start = s + 60*m + 3600*h
    
t, k = map(int, input().split())
time = t * (100-k) // 100
if now + time <= start:
    print(1)
else:
    print(0)