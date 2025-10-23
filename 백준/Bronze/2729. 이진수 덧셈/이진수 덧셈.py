# bronzeI_2729
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    a = int(a, 2)
    b = int(b, 2)
    
    result = bin(a+b)
    print(result[2:])