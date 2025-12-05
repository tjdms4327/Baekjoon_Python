import sys

d = int(input())
for line in sys.stdin.read().splitlines():
    x = int(line)
    if d > x:
        d += x
    else:
        print(d)
        sys.exit()