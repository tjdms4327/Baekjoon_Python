# bronzeIII_32305
import sys
input = sys.stdin.readline
from math import ceil

a, b = map(int, input().split())
d = int(input())
apple = a * b
print(ceil(apple/12) * d)