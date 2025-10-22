# bronzeII_19946
import sys, math
input = sys.stdin.readline

num = int(input())
while num % 2 == 0:
    num //= 2

num += 1
print(int(math.log2(num)))