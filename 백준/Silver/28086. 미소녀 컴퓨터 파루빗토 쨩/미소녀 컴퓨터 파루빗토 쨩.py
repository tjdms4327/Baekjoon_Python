import sys
input = sys.stdin.readline

line = input().strip()
for i in range(1, len(line)):
    if line[i] in '+-*/':
        operator = line[i]
        num1 = line[:i]
        num2 = line[i+1:]
        break

num1 = int(num1, 8)
num2 = int(num2, 8)

if operator == '/' and num2 == 0:
    print('invalid')
else:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 // num2

    print(format(result, 'o'))