# bronzeI_4539
import sys, math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    
    d = 10
    while x >= d:
        x = ((x + d//2) // d) * d
        d *= 10

    print(x)