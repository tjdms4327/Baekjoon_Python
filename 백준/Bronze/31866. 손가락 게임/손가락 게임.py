import sys
input = sys.stdin.readline

def win_x(x, y):
    if (x == 0 and y == 2)\
        or (x == 2 and y == 5)\
        or (x == 5 and y == 0):
            return True
    else:
        return False

a, b = map(int, input().split())

if (a not in [0,2,5] and b not in [0,2,5]) or a==b:
    print('=')
elif a not in [0,2,5]:
    print('<')
elif b not in [0,2,5]:
    print('>')
elif win_x(a, b):
    print('>')
else:
    print('<')