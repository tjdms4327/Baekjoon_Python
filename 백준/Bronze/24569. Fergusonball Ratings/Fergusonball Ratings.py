# bronzeIII_24569
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
count = 0
for _ in range(n):
    a, b = int(input()), int(input())
    star_rating = 5*a - 3*b
    
    if star_rating > 40:
        count += 1
print(str(count) + ('+' if count == n else ''))