# bronzeIII_31776
import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    t1, t2, t3 = map(int, input().split())
    if t2 == -1: t2 = float('inf')
    if t3 == -1: t3 = float('inf')
    
    if t1 != -1:
        if t1 <= t2 <= t3:
            count += 1
    else:
        continue
print(count)