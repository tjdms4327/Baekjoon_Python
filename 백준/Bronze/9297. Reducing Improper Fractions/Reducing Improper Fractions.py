import sys
input = sys.stdin.readline
import math

for case in range(1, int(input())+1):
    a, b = map(int, input().split())
    quotient, remainder = divmod(a, b)
    
    print(f'Case {case}:', end = ' ')
    if quotient == 0 and remainder == 0:
        print(0)
    elif quotient == 0:
        print(f'{remainder}/{b}')
    elif remainder == 0:
        print(quotient)
    else:
        print(f'{quotient} {remainder}/{b}')