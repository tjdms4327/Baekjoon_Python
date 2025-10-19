# bronzeI_2033
import sys
input = sys.stdin.readline

n = int(input())

temp = 10
while n > temp:
    n = (n + temp//2) // temp * temp
    temp *= 10
print(n)