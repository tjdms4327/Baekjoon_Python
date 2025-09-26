# bronzeII_7120
import sys
input = sys.stdin.readline

s = input().strip()
prev = ''
for i in s:
    if i != prev:
        print(prev, end='')
        prev = i
print(prev, end='') # 마지막 요소 처리