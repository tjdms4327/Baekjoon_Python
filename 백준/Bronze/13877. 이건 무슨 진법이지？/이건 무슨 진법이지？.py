import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    i, num = input().strip().split()
    
    if any(c not in '01234567' for c in num):
        octal = 0
    else:
        octal = int(num, 8)
    
    decimal = int(num)
    hexa = int(num, 16)
    
    print(i, octal, decimal, hexa)