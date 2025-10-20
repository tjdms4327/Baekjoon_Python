# bronzeII_4564
import sys
input = sys.stdin.readline
from math import prod

while True:  
    n = int(input())
    if n == 0:
        break
    
    while True:
        print(n, end=' ')
        if n < 10: 
            break
        
        lst = list(map(int, str(n)))
        n = prod(lst)
    print()