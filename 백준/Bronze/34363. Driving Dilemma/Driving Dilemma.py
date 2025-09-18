import sys
input = sys.stdin.readline

v = int(input())
d = float(input())
t = float(input())

time = (d / 5280) / v * 3600
if time <= t: 
    print('MADE IT')
else:
    print('FAILED TEST')