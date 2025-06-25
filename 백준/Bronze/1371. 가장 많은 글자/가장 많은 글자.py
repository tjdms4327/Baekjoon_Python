import sys
input=sys.stdin.read

import string
lowercase = list(string.ascii_lowercase)

s=input().strip()
alph, num='',0
for i in lowercase:
    c=s.count(i)
    if c>num:
        alph=i
        num=c
    elif c==num:
        alph+=i
print(alph)