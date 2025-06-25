import sys
input = sys.stdin.readline

from math import sqrt

def isprime(n):
    if n==1:
        return 'It is a prime word.'
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 'It is not a prime word.'
    return 'It is a prime word.'

s=input().strip()
tot=0
for i in s:
    if i.isupper():
        tot+=ord(i)-38
    else:
        tot+=ord(i)-96
result=isprime(tot)
print(result)