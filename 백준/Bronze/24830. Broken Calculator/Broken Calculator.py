# bronzeIII_24830
import sys
input = sys.stdin.readline
from math import ceil

def calculator(a, op, b):
    global pre
    a = int(a) ; b = int(b)
    
    if op == '+':
        pre = (a+b) - pre
        return pre
    elif op == '-':
        pre *= (a-b)
    elif op == '*':
        pre = (a*b)**2
    elif op == '/':
        pre = ceil(a/2)
        
    return pre
    
n = int(input())
pre = 1
for _ in range(n):
    a, op, b = input().strip().split()
    print(calculator(a, op, b))