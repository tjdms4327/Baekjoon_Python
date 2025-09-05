import sys
input = sys.stdin.readline

import math

for case in range(1, int(input())+1):
    b, w = map(float, input().split())
    V = sum([4 / 3 * math.pi * float(input())**3 for _ in range(int(b))]) / 1000
    
    print(f'Data Set {case}:')
    if w <= V:
        print('Yes\n')
    else: print('No\n')