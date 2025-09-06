import sys
input = sys.stdin.readline

for case in range(int(input())):
    y, m, d = map(int, input().split())
    if y < 2007-18: 
        print('Yes')
    elif y == 2007-18:
        if m == 1: print('Yes')
        elif m == 2 and d <= 27:
            print('Yes')
        else:
            print('No')
    else: 
        print('No')