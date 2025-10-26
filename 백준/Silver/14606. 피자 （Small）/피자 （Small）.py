# silverV_14606
import sys
input = sys.stdin.readline

def enjoy(n):
    if n == 1:
        return 0
    return (n//2)*(n - n//2) + enjoy(n//2) + enjoy(n - n//2)
        

n = int(input())
print(enjoy(n))
