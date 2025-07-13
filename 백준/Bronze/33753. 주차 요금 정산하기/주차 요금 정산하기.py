import sys
input=sys.stdin.readline

from math import ceil

a,b,c=map(int, input().strip().split())
t=int(input().strip())

fee=0
if t<=30: fee=a
else:
    fee=a+ceil((t-30)/b)*c
print(fee)