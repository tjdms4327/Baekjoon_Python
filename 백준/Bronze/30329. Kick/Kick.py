import sys
input = sys.stdin.readline

import re

s = input().strip()
target = "kick"
cnt = 0
for i in range(len(s) - len(target) + 1):
    if s[i:i+len(target)] == target:
        cnt += 1
print(cnt)