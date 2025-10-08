# bronzeIII_29070
import sys
input = sys.stdin.readline
from math import ceil

a, b, h, w = map(int, input().split())
print(ceil(h/a) * ceil(w/b))