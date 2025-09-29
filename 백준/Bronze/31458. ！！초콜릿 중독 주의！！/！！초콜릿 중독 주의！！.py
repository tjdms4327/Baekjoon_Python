# bronzeII_31458
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().strip())
    
    num_idx = next(i for i, ch in enumerate(s) if ch in ('0', '1'))
    num = int(s[num_idx])
    left, right = num_idx, len(s) - num_idx - 1
    if right: 
        num = 1
    if left % 2 == 1:
        if num == 0:
            num = 1
        else:
            num = 0
    print(num)