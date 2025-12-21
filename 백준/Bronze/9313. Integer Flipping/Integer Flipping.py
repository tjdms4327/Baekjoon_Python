import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    x = bin(n)[2:].zfill(32)[::-1]
    print(int(x, 2))