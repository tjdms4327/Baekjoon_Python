import sys
input = sys.stdin.readline
from collections import Counter

a = Counter(input().strip())
b = Counter(input().strip())

result = []
for ch in set(a + b):
    result.append(ch * max(a[ch], b[ch]))
print(''.join(result))