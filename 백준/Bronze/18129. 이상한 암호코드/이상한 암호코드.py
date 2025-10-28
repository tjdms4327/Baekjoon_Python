# bronzeI_18129
import sys
input = sys.stdin.readline
from itertools import groupby

s, k = input().strip().split()
s = s.lower()
k = int(k)

groups = [''.join(g) for _, g in groupby(s)]

visited = set()
result = ''
for group in groups:
    if group[0] in visited:
        continue
    
    if len(group) >= k:
        result += '1'
    else:
        result += '0'
    visited.add(group[0])
print(result)