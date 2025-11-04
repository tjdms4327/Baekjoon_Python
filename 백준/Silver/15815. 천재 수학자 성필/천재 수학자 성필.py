# silverIII_15815
import sys
input = sys.stdin.readline

expr = input().strip()

stack = []
for ch in expr:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(int(a / b))

print(*stack)