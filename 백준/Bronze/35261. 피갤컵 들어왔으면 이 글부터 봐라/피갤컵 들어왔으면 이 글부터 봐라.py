import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

best = 5
for i in range(0, n-4):
    slice = s[i:i+5]
    diff = sum(slice[i]!='eagle'[i] for i  in range(5))
    best = min(best, diff)
    
print(best)
    