# bronzeIII_25024
import sys
input = sys.stdin.readline

def possible_time(x, y):
    if 0<=x<=23 and 0<=y<=59:
        return 'Yes'
    return 'No'

def possible_date(x, y):
    if (x == 2 and 1<=y<=29) \
        or (x in [1, 3, 5, 7, 8, 10, 12] and 1<=y<=31) \
        or (x in [4, 6, 9, 11] and 1<=y<=30):
            return 'Yes'
    return 'No'

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(possible_time(x, y), possible_date(x, y))
    