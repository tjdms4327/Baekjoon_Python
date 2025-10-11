# bronzeIII_25869
import sys
input = sys.stdin.readline

w, h, d = map(int, input().split())

side1, side2= w-2*d, h-2*d
if side1 <= 0 or side2 <= 0:
    print(0)
else:
    print(side1*side2)