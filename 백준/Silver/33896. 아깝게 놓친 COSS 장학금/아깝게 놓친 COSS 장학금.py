import sys, math
input = sys.stdin.readline

n = int(input())

COSS = []
for _ in range(n):
    name, *line = input().strip().split()
    score, risk, cost = map(int, line)
    
    S = math.floor((score)**3 / (cost*(risk+1)))
    COSS.append((S, cost, name))
    
COSS.sort(key = lambda x:(-x[0], x[1], x[2]))
print(COSS[1][-1])