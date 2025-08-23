import sys 
input = sys.stdin.readline

equation = list(input().strip().split())


def change_operator(num1, operater, num2):
    n1 = int(num1)
    n2 = int(num2)
    if operater == '*':
        return n1*n2
    elif operater == '/':
        if n1<0 or n2<0:
            n1 = abs(n1); n2 = abs(n2)
            return (-1)*(n1//n2)
        return n1//n2
    elif operater == '+':
        return n1+n2
    elif operater == '-':
        return n1-n2

first_1 = change_operator(*equation[:3])
first_2 = change_operator(first_1, *equation[3:])

second_1 = change_operator(*equation[2:])
second_2 = change_operator(*equation[:2], second_1)

print(min(first_2, second_2), max(first_2, second_2), sep='\n')