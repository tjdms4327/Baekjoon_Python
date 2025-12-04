import sys, math
input = sys.stdin.readline

n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

time = (m/x + (n-m)/y) / 60
if time <= t:
    print(0)
else:
    print(math.ceil(time-t))