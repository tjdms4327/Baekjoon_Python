import sys
input = sys.stdin.readline

r, b = map(int, input().split())
total = r + b
for i in range(1, total+1):
    if total % i == 0:
        side1, side2 = i, total // i
        if (side1 - 2) * (side2 - 2) == b:
            print(max(side1, side2), min(side1, side2))
            sys.exit()