import sys
input=sys.stdin.readline

import math

n=int(input())
for i in range(1, n+1):
    default='yes'
    lines=list(map(int, input().split()))
    lines.sort()
    if lines[-1]**2!= lines[0]**2+lines[1]**2:
        default='no'
    print(f'Scenario #{i}:\n{default}')
    print()
    