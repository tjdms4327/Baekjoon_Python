import sys
input = sys.stdin.readline

import re

n = int(input())
s = input().strip()
parts = re.split(re.escape('b'), s)

tot = sum(len(i) for i in parts if len(i) >= 2)
print(tot)