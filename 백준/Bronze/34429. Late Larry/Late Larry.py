import sys
input = sys.stdin.readline

T, d = input().strip().split()
h, m = map(int, T.split(':'))
t = int(input())

if d == 'AM':
    if h == 12:
        h = 0
else:
    if h != 12:
        h += 12
        
time = 60*h + m - t
if time < 0:
    time += 24*60

if time < 12*60:
    d = 'AM'
    h = time//60
    if h == 0: 
        h = 12
else:
    d = 'PM'
    h = (time//60) - 12
    if h == 0:
        h = 12
m = time % 60
print(f'{h}:{m:02d} {d}')