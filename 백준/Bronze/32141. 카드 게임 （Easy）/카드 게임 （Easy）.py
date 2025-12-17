import sys, math
input = sys.stdin.readline

n, h = map(int, input().split())
cards = list(map(int, input().split()))

if sum(cards) < h:
    print(-1)
elif sum(cards) == h:
    print(n)
else:
    count = 0
    for x in cards:
        if h > 0:
            count += 1
            h -= x 
        else:
            break
    print(count)