# bronzeII_4998
import sys
from math import ceil, log

for line in sys.stdin.read().splitlines():
    n, b, m = map(float, line.split())
    
    percent = 1 + b/100
    y = ceil(log(m/n) / log(percent))
    print(y)