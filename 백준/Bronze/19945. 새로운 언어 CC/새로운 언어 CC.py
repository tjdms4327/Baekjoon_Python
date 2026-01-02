import sys
input = sys.stdin.readline

n = int(input())
if n==0:
    print(1)
elif n > 0:
    print(n.bit_length())
else:
    print(32)