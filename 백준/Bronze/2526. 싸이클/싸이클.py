# bronzeI_2526
import sys
input = sys.stdin.readline

n, p = map(int, input().split())

result = []
cur = n
while True:
    cur = cur*n % p
    
    if cur in result:
        break
    result.append(cur)    
    
print(len(result) - result.index(cur))