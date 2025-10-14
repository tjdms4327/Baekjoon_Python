# bronzeII_15841
import sys
input = sys.stdin.readline

cows = [0] + [1, 1]
while True:
    x = int(input())
    if x == -1:
        break
    
    for i in range(len(cows), x+1):
        cows.append(cows[i-1] + cows[i-2])
    y = cows[x]
    print(f'Hour {x}: {y} cow(s) affected')
