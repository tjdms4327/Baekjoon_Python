# bronzeII_24389
import sys
input = sys.stdin.readline

n = int(input())

mask = (1 << 32) - 1

a = n & mask
b = ((~n) + 1) & mask
x = (a ^ b).bit_count()
print(x)