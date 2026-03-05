import sys
input = sys.stdin.readline

n = int(input())
O = []
for _ in range(n):
    operation, o = input().strip().split()
    operand = int(o)
    O.append((operation, operand))

def operate(x, operation, k):
    if operation == 'ADD':
        x += k
    elif operation == 'SUBTRACT':
        x -= k
    elif operation == 'MULTIPLY':
        x *= k        
    elif operation == 'DIVIDE':
        if x % k != 0:
            return -1
        x //= k
    return x


count = 0
for i in range(1, 101):
    x = i
    for operation, o in O:
        x = operate(x, operation, o)
        if x < 0:
            count += 1 
            break

print(count)