# bronzeII_5987
import sys
input = sys.stdin.readline

z = int(input())
for _ in range(z):
    n, c, s = input().strip().split()
    n, c = int(n), int(c)
    
    for _ in range(c):
        tmp = s[n:]
        s = tmp + s
    print(s)