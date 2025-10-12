# bronzeIII_24805
import sys
input = sys.stdin.readline
from math import ceil

a, b, h = map(int, input().split())
if h <= a:
    print(1)
else:
    print(ceil((h-a)/(a-b)) + 1)