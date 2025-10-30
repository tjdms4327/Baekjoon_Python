# silverV_22403
import sys
input = sys.stdin.readline

n = int(input())

stack = []
count = 0
for _ in range(n):
    s = input().strip()
    
    if s == 'A':
        stack.append(s)
    else:
        if stack and stack[-1] == 'A':
            stack.pop()
        else:
            print('NO')
            sys.exit()

if stack:
    print('NO')
else:
    print('YES')
