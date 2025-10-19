# bronzeI_14467
import sys
input = sys.stdin.readline

cows = {}

cross = 0
n = int(input())
for _ in range(n):
    num, pos = map(int, input().split())
    
    if num in cows:
        if pos != cows[num]:
            cross += 1
    cows[num] = pos

print(cross)