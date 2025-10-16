# bronzeII_6359
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    room = [0] * (n+1)
    
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            room[j] += 1
    
    print(sum(1 for i in room if i%2==1))