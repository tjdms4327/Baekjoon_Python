# bronzeI_12833
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c % 2 == 0:
    print(a)
else:
    print(a ^ b)