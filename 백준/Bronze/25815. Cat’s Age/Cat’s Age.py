# bronzeIII_25815
import sys
input = sys.stdin.readline

def catage_to_humanage(y,m):
    if y < 1:
        human_y = 0
        human_m = 15*m
    elif y < 2:
        human_y = 15
        human_m = 9*m
    else:
        human_y = 15 + 9 + (y-2)*4
        human_m = 4*m
        
    if human_m >= 12:
        human_y += (human_m//12)
        human_m %= 12
    
    return human_y, human_m

y, m = map(int, input().split())
print(*catage_to_humanage(y, m))