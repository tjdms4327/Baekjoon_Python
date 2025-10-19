# bronzeI_1952
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def recursive(n, m):
    if n == 2 and m > 1:
        return 2
    if n > 1 and m == 2:  
        return 3  
    if m == 1 and n > 1:  
        return 1  
    if n == 1:  
        return 0  

    return 4 + recursive(n - 2, m - 2)  

print(recursive(n, m))