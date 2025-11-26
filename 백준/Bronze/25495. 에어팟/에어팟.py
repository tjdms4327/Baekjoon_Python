import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

total = 0
prev_cost = 0
prev = None
for cur in A:
    if prev != cur:
        cost = 2
    else:
        cost = prev_cost * 2
    total += cost
    
    if total >= 100:
        total = 0
        prev_cost = 0
        prev = None
    else:
        prev_cost = cost
        prev = cur
    
print(total)