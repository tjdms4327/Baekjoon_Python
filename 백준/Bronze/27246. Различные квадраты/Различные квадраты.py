# bronzeIII_27246
import sys
input = sys.stdin.readline

n = int(input())
square_count = 0
k = 1
while n >= k**2:
    n -= k**2
    square_count += 1
    k += 1
print(square_count)