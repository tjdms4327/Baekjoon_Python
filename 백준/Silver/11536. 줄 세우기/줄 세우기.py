import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

if sorted(names) == names:
    print('INCREASING')
elif sorted(names, reverse=True) == names:
    print('DECREASING')
else:
    print('NEITHER')