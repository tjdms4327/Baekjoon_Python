import sys
input=sys.stdin.readline

t=[int(input().strip()) for _ in range(4)]
if sum(t)+300<=1800: print('Yes')
else: print('No')