import sys
input = sys.stdin.readline

t, d, m = map(int, input().split())

if m == 0:
    if t <= d:
        print('Y')
    else:
        print('N')
else:
    Y = [int(input()) for _ in range(m)]

    diff = max(Y[0], d - Y[-1])
    for i in range(1, m):
        diff = max(diff, Y[i]-Y[i-1])
        
    if diff >= t:
        print('Y')
    else:
        print('N')