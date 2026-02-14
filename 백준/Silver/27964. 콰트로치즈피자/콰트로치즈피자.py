import sys
input = sys.stdin.readline

n = int(input())
topping = set(input().strip().split())

count = 0
for x in topping:
    if x.endswith('Cheese'):
        count += 1

if count >= 4:
    print('yummy')
else:
    print('sad')