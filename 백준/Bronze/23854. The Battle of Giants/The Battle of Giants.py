import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

one, two = a//3, b//3
a -= one*3
b -= two*3

if a!=b:
    print(-1)
else:
    print(one, a, two)