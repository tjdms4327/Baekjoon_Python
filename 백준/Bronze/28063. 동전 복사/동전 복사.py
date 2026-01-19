import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())

if n==1:
    print(0)
else:
    if x in [1, n] and y in [1, n]:
        print(2)
    elif x in [1, n] or y in [1, n]:
        print(3)
    else:
        print(4)