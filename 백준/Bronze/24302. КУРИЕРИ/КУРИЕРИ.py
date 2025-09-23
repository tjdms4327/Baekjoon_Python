# bronzeIII_24302.py
import sys
input = sys.stdin.readline

def select_one(distance):
    if distance <= 5:
        return 400
    elif distance <= 10:
        return 700
    elif distance <= 20:
        return 1200
    elif distance <= 30:
        return 1700
    else:
        return distance*57
    
def select_two(distance):
    if distance <= 2:
        return (1 + distance) * 90
    elif distance <= 5:
        return 100 + distance*85
    elif distance <= 20:
        return 100 + 25 + distance*80
    elif distance <= 40:
        return 300 + 25 + distance*70
    else:
        return 900 + 25 + distance*55
    

a, b = map(int, input().split())
a //= 1000
b //= 1000
min_a = min(select_one(a), select_two(a))
min_b = min(select_one(b), select_two(b))
print(f'{(min_a + min_b)//100}.{(min_a + min_b)%100:02d}')