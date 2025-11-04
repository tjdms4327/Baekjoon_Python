# silverII_5397
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = list(input().strip())
    
    left, right = [], []
    for ch in l:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch =='>':
            if right:
                left.append(right.pop())
        elif ch =='-':
            if left:
                left.pop()
        else:
            left.append(ch)
    
    left.extend(reversed(right))
    print(''.join(left))