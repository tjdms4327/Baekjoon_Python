# bronzeII_34431
import sys
input = sys.stdin.readline
from math import ceil

w = int(input())
m = int(input())
c = int(input())

print(ceil((c*w*m) / (60*1000*100)))