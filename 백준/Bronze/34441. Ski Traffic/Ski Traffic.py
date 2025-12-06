import sys
input = sys.stdin.readline

input()
h, m = map(int, input().split(':'))
day = input().strip()
weather = int(input())
front = int(input())
holiday = int(input())

temp = 1
if day in ['sat', 'sun']:
    temp *= 2
if weather == 1:
    temp *= 2
if front == 1:
    temp *= 3
if holiday == 1:
    temp *= 3

t = (60*h + m) * temp
h = t // 60
m = t % 60
print(f'{h}:{m:02d}')