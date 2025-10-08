# bronzeIII_22150
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    
    n = lst[0]
    eat = False
    for i in range(1, 2*n, 2):
        if lst[i] + lst[i+1] == n:
            continue
        else:
            eat = True
            break
    if eat:
        print('yes')
    else:
        print('no')