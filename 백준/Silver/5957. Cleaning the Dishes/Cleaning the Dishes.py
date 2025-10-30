# silverV_5957
import sys
input = sys.stdin.readline

n = int(input())
dish_left = list(range(n, 0, -1))
dish_right = []
clean = []

while True:
    line = input().strip()
    if not line:
        break
    
    c, d = map(int, line.split())
    if c == 1:
        for i in range(d):
            if dish_left:
                dish_right.append(dish_left[-1])
                dish_left.pop()
    else: # c==2
        for i in range(d):
            if dish_right:
                clean.append(dish_right[-1])
                dish_right.pop()

print(*clean[::-1], sep='\n')