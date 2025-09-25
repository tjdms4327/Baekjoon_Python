# bronzeII_4678
import sys
input = sys.stdin.readline

while True:  
    n = input().strip()
    if n == '0': break
    
    
    result = 0
    for i in range(1, len(n)+1):
        result += (2**i - 1) * int(n[(-1)*i])
    print(result)