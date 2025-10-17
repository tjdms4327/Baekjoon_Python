# bronzeII_22341
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a, b = n, n

for i in range(c):
    x, y = map(int, input().split())
    
    if x > a or y > b:
        continue
    area_up = a * y
    area_left = b * x
    if area_up >= area_left:
        b = y
    else:
        a = x
print(a*b)