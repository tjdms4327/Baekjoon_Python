# bronzeII_5176
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p, m = map(int, input().split())
    
    count = 0
    seat = []
    for _ in range(p):
        want = int(input())
        if want in seat:
            count += 1
        else:
            seat.append(want)
    print(count)