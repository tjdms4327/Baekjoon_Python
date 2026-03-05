import sys
input = sys.stdin.readline
import math

t = int(input())
for _ in range(t):
    project, team, mid = map(int, input().split())
    
    need = 90*100 - project*15 - team*20 - mid*25
    f = math.ceil(need / 40)
    
    if 0 <= f <= 100:
        print(f)
    else:
        print('impossible')