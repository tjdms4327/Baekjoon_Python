# bronzeIII_18005
import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 1:
    print(0)
elif n % 4 == 0:
    print(2)
else:
    print(1)