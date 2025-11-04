# silverIV_24448
import sys
input = sys.stdin.readline

q = int(input())
stack = []
for _ in range(q):
    s = input().strip()
    
    if stack and s=='READ':
        print(stack.pop())
    else:
        stack.append(s)