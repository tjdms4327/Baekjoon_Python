import sys
input=sys.stdin.readline

n=int(input())
x=int(input())
while x!=0:
    if x%n==0:
        print(f'{x} is a multiple of {n}.')
    else:
        print(f'{x} is NOT a multiple of {n}.')
    x=int(input())