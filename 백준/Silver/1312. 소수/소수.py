import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

r = a % b
for _ in range(n):
    r *= 10
    digit = r // b
    r %= b
print(digit)