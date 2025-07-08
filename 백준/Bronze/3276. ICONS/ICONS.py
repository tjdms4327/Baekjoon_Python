import sys
input=sys.stdin.readline
from math import ceil

n=int(input().strip())
min_sum=float('inf')
ans=[]
for row in range(1, int(n**0.5)+1):
    col=ceil(n/row)
    sum_rc=row+col
    if sum_rc<min_sum: 
        min_sum=sum_rc
        ans=[row, col]
print(*ans, sep=' ')