import sys
input = sys.stdin.readline
import math


n = int(input())

f = math.factorial(n)
print(str(f).count('0'))