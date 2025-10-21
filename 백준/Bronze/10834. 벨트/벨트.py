# bronzeII_10834
import sys
input = sys.stdin.readline
from fractions import Fraction

direction = 0
speed = Fraction(1, 1)

m = int(input())
for _ in range(m):
    a, b, belt = map(int, input().split())
    
    if belt == 1:
        direction ^= 1
    speed *= Fraction(b, a)

print(direction, speed.numerator)