# bronzeIII_30886
import sys
input = sys.stdin.readline
from math import sqrt, pi

a = int(input())
side = 2 + sqrt(a/pi)*2
print(side**2)