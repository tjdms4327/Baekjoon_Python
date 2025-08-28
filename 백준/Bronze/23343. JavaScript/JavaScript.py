import sys
input = sys.stdin.readline

x, y = input().strip().split()

if x.isdigit() and y.isdigit():
    print(int(x) - int(y))
else:
    print('NaN')