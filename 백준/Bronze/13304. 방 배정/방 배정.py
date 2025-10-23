# bronzeII_13304
import sys
input = sys.stdin.readline
from math import ceil

room = [0] * 5

n, k = map(int, input().split())
for _ in range(n):
    s, y = map(int, input().split())
    
    if y <= 2:
        room[0] += 1
    else:
        room[((y - 3) // 2) * 2 + s + 1] += 1
print(sum(ceil(x/k) for x in room))