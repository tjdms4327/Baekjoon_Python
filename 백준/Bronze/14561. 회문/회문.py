# bronzeII_14561
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, n = map(int, input().split())
    
    result = []
    while a >= n:
        result.append(a%n)
        a //= n
    result.append(a)
    
    if result == result[::-1]:
        print(1)
    else:
        print(0)