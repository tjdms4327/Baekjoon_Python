import sys
input = sys.stdin.readline

n = int(input())

length = len(str(n))
if length == 1:
    print(1)
elif int('1'*length) <= n:
    print(length)
else:
    print(length-1)