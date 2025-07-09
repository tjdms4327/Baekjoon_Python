import sys
input=sys.stdin.readline

import math

while True:
    s=input().strip()
    if s=='0': break

    length=len(s)
    num=0
    for i in s:
        cand=int(i)
        num+=cand*math.factorial(length)
        length-=1
    print(num)