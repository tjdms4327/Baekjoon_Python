# bronzeIII_20359
import sys
input = sys.stdin.readline

n = int(input())

p = 0
while n%2==0:
    n//=2
    p += 1
    
o = n
print(o, p)