import sys
input=sys.stdin.readline

g, gb, y, r, ry=map(int, input().split())
t=int(input())



on=g+gb+y+r+ry
on_d=t//on
left=t%on
green, yellow, red=on_d*(g+gb/2), on_d*(y+ry), on_d*(r+ry)

if left > 0: # green
    if left >= g:
        green += g
        left -= g
    else:
        green += left
        left = 0
if left > 0: # green 깜빡임
    if left >= gb:
        green += gb // 2
        left -= gb
    else:
        green += left / 2
        left = 0
if left > 0: # yellow
    if left >= y:
        yellow += y
        left -= y
    else:
        yellow += left
        left = 0
if left > 0: # red
    if left >= r:
        red += r
        left -= r
    else:
        red += left
        left = 0
if left > 0: # yellow+red
    if left >= ry:
        red += ry
        yellow += ry
        left -= ry
    else:
        red += left
        yellow += left
        left = 0

print(int(red), int(yellow), int(green))
