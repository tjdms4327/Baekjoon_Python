import sys
input = sys.stdin.readline

yard = 1296

n = int(input())
for _ in range(n):
    i = int(input())
    
    area = 0
    for _ in range(i):
        s, r = map(int, input().split())
        area += s*r

    print(yard//area, (yard*2)//area, (yard*3)//area)