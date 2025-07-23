import sys
input=sys.stdin.readline

from collections import Counter

n=int(input())
for i in range(1, n+1):
    a=Counter(input())
    b=Counter(input())
    intersection=a&b
    diff=sum((a-intersection).values())+sum((b-intersection).values())
    print(f'Case #{i}: {diff}')