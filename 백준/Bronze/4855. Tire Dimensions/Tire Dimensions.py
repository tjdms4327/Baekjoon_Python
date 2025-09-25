# bronzeII_4855
import sys
input = sys.stdin.readline
import math

for line in sys.stdin:
    s = line.strip()
    if not s: 
        continue
    
    parts = s.split()
    w = int(parts[1])
    ratio = int(parts[3])
    rim = int(parts[-1])
    
    h = w * ratio / 100
    diameter = 2 * h + rim * 25.4
    circumstance = math.pi * diameter / 10
    print(f'{s}: {round(circumstance)}')