import sys
input = sys.stdin.readline
from math import prod

n = list(map(int, input().strip()))
for i in range(1, len(n)):
    front = prod(n[:i])
    back = prod(n[i:])
    
    if front == back:
        print('YES')
        sys.exit()
print('NO')