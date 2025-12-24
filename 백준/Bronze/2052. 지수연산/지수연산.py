import sys
input = sys.stdin.readline
from decimal import Decimal, getcontext

n = int(input())

getcontext().prec = n+10
result = Decimal(1) / (Decimal(2)**n)
print(format(result, 'f'))