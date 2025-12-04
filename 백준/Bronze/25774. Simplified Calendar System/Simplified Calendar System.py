import sys
input = sys.stdin.readline

d1, m1, y1, n1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

days = (y2-y1)*360 + (m2-m1)*30 + (d2-d1)
days %= 7
days += n1
if days > 7:
    days = (days-1)%7 + 1
print(days)