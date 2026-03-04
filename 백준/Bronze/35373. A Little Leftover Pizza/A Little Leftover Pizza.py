import sys
input = sys.stdin.readline
import math

n = int(input())

left_slice = {'S':0, 'M':0, 'L':0}
for _ in range(n):
    size, left = input().strip().split()
    left = int(left)
    left_slice[size] += left
    
    
box = 0
for size, slice in left_slice.items():
    if size == 'S':
        box += math.ceil(slice / 6)
    elif size == 'M':
        box += math.ceil(slice / 8)
    else:
        box += math.ceil(slice / 12)
        
print(box)