import sys
input = sys.stdin.readline
from decimal import Decimal, getcontext

getcontext().prec = 30 # 소수점 정밀도 설정

a, b, c = map(Decimal, input().split())
print(a*b/c)