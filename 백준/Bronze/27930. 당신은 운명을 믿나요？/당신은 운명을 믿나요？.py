# bronzeI_27930
import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()

yonsei = deque('YONSEI')
korea = deque('KOREA')
for ch in s:
    if not yonsei or not korea:
        break
    
    if ch == yonsei[0]:
        yonsei.popleft()
    if ch == korea[0]:
        korea.popleft()

if not yonsei:
    print('YONSEI')
else:
    print('KOREA')