# bronzeII_22341
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a, b = n, n

for i in range(c):
    x, y = map(int, input().split())
    
    if x >= a or y >= b:
        continue
    
    area_horizontal = x * b 
    area_vertical = a * y 
    if area_vertical > area_horizontal:
        b = y
    else:
        a = x
        
print(a * b)