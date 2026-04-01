# silverIII_11899
import sys
input = sys.stdin.readline

s = input().strip()

stack = []
for ch in s:
    if stack and (stack[-1]=='(' and ch == ')'):
        stack.pop()
    else:
        stack.append(ch)
print(len(stack))