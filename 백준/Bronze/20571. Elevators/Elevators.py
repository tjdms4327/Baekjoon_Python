# bronzeIII_20571
import sys
input = sys.stdin.readline

s, n = input().strip().split()
n = int(n)

if n == 1:
    print(0)
    exit()
    
if s == 'residential':
    if n < 6:
        print(1)
    elif n < 11:
        print(2)
    elif n < 16:
        print(3)
    else:
        print(4)
elif s == 'commercial':
    if n < 8:
        print(1)
    elif n < 15:
        print(2)
    else:
        print(3)  
else:
    if n < 5:
        print(1)
    elif n < 9:
        print(2)
    elif n < 13:
        print(3)
    elif n < 17:
        print(4)
    else:
        print(5)