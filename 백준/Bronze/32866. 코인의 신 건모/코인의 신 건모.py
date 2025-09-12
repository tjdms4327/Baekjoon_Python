import sys
input = sys.stdin.readline

n = int(input())
x = int(input())

now = n * (1 - x/100)
print((n / now - 1) * 100)