# bronzeII_8741
import sys
input = sys.stdin.readline

k = int(input())

max_n = 2**k - 1
Sum = max_n * (max_n + 1) // 2
print(bin(Sum)[2:])