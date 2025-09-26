# bronzeII_6736
import sys
input = sys.stdin.readline
from math import factorial

t = int(input())
for _ in range(t):
    day, n = input().strip().split()
    
    num = str(factorial(int(day)))
    print(num.count(n))