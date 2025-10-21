# bronzeI_4150
import sys
input = sys.stdin.readline

n = int(input())

if n in [1, 2]:
    print(1)
else:
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b
    print(b)