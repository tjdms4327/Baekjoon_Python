# silverV_16815
import sys
input = sys.stdin.readline

s = input().strip()

stack = []
for ch in s:
    if ch == '(' or ch == '*':
        stack.append(ch)
    else: # ch == ')'
        if stack[-1] == '(':
            stack.pop()
        else:
            break
        
print(stack.count('('))