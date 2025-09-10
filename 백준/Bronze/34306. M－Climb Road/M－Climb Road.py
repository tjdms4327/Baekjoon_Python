import sys
input = sys.stdin.readline

from math import floor

w = int(input())
n = int(input())

length = w * 5280
watergun = floor(length / n)
print(watergun)