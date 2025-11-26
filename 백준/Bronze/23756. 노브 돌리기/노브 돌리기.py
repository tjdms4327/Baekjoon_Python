import sys
input = sys.stdin.readline

n = int(input())
a0 = int(input())

total = 0
for _ in range(n):
    x = int(input())
    
    cand1 = abs(x-a0)
    cand2 = 360 - cand1
    total += min(cand1, cand2)
    
    a0 = x
    
print(total)