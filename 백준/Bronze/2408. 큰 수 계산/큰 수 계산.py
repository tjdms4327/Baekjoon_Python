import sys
input = sys.stdin.readline

n = int(input())

expr = []
for _ in range(2*n-1):
    x = input().strip()
    if x in "+-*/":
        expr.append(x)
    else:
        expr.append(int(x))

temp = [expr[0]]
idx = 1
while idx < len(expr):
    op = expr[idx]
    b = expr[idx+1]
    
    if op == '*':
        temp.append(temp.pop() * b)
    elif op == '/':
        a = temp.pop()
        temp.append(a // b)
    else:
        temp.append(op)
        temp.append(b)
    idx += 2

res = temp[0]
idx = 1
while idx < len(temp):
    op = temp[idx]
    b = temp[idx+1]
    
    if op == '+':
        res += b
    else:
        res -= b
    idx += 2
print(res)