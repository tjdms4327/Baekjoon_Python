# bronzeII_4141
import sys
input = sys.stdin.readline

def al_to_num(s):
    result = ''
    for i in s:
        if i in 'ABC':
            result += '2'
        elif i in 'DEF':
            result += '3'
        elif i in 'GHI':
            result += '4'
        elif i in 'JKL':
            result += '5'
        elif i in 'MNO':
            result += '6'
        elif i in 'PQRS':
            result += '7'
        elif i in 'TUV':
            result += '8'
        else:
            result += '9'
    return result
        
n = int(input())
for _ in range(n):
    s = input().strip().upper()
    phone_num = al_to_num(s)
    
    if phone_num == phone_num[::-1]:
        print('YES')
    else:
        print('NO')   