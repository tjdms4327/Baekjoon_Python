import sys
input = sys.stdin.readline

t, j = map(int, input().split())
while True:
    j += t
    if j >= 5: 
        print('yt')
        exit(0)
    t += j
    if t >= 5:
        print('yj')
        exit(0)
    