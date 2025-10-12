# bronzeIII_21167
import sys
from math import sqrt

for line in sys.stdin.read().splitlines():
    r, s = map(float, line.split())
    
    v = sqrt(r*(s+.16) / 0.067)
    print(int(round(v)))