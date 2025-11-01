# bronzeII_16462
import sys, math
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    s = input().strip().replace('6', '9').replace('0', '9')
    s = int(s)
    
    if s > 100:
        s = 100
    score.append(s)
    
avg = sum(score) / n
print(math.floor(avg + 0.5))