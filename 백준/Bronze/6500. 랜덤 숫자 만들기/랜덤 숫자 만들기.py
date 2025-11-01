# bronzeII_6500
import sys
input = sys.stdin.readline

while True:  
    a0 = input().strip()
    if a0 == '0':
        break
    
    n = len(a0)
    seen = set()
    while a0 not in seen:
        seen.add(a0)
        num = int(a0) ** 2
        num_str = str(num).zfill(2*n)
        a0 = num_str[n//2 : n//2 + n]
    print(len(seen))