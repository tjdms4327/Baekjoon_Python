# bronzeII_3943
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    max_n = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
            max_n = max(n, max_n)
            
    print(max_n)