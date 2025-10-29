# silverV_32200
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
A = list(map(int, input().split()))

meal_count = 0
best_left = 0
for a in A:
    if a < x:
        best_left += a
        continue
    
    count = a // x
    left = a % x
    
    if (y-x) * count < left:
        best_left += left - (y-x) * count
        
    meal_count += count
    
print(meal_count)
print(best_left)