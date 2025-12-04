import sys, math
input = sys.stdin.readline

while True:
    d, e = map(int, input().split())
    if d == e == 0:
        break
    
    min_e = float('inf')
    for x in range(d):
        y = d - x
        price = abs(math.sqrt(x**2 + y**2) - e)
        min_e = min(min_e, price)
    print(min_e)