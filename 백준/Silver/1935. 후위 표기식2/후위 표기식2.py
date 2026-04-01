# silverIII_1935
import sys
input = sys.stdin.readline

stack = []

n = int(input())
expr = input().strip()
values = [int(input()) for _ in range(n)]

for ch in expr:
    if 'A' <= ch <= 'Z':
        stack.append(values[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
        elif ch == '*':
            stack.append(a*b)
        elif ch == '/':
            stack.append(a/b)
            
print(f"{stack[0]:.2f}")