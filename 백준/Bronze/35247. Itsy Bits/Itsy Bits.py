import sys
input = sys.stdin.readline
import math

n = int(input())

min_bit = math.ceil(math.log2(n+1))

ans = 1
while ans < min_bit:
    ans *= 2

if ans == 1:
    print('1 bit')
else:
    print(f'{ans} bits')