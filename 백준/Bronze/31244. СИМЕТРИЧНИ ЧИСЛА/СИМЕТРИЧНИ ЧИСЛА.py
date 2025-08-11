import sys
input=sys.stdin.readline

a, b, c=input().strip().split()

if a==b==c: print(a+b+c)
elif b==c: print(a+b+c+a)
elif a==c: print(a+b+c)
else: print(a+b+c+b+a)
