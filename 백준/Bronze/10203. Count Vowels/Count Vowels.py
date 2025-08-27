import sys
input = sys.stdin.readline

import re

n = int(input())
for _ in range(n):
    s = input().strip()
    cnt = len(re.findall(f'[aeiou]', s.lower()))
    print(f'The number of vowels in {s} is {cnt}.')