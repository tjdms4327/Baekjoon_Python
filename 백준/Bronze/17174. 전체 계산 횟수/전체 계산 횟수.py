import sys
input = sys.stdin.readline

n, m = map(int, input().split())

count = n
while n // m > 0:
    n //= m
    count += n
print(count)