import sys, math
input = sys.stdin.readline

b, w = map(int, input().split())

if b == w == 0:
    print('Impossible')
else:
    for side in range(math.isqrt(b+w)+1, 0, -1):
        tot = side**2
        if side % 2== 0:
            if min(b, w) >= (tot)//2:
                print(side)
                break
        else:
            if min(b, w) >= tot//2 and max(b,w)>= tot//2+1:
                print(side)
                break
        