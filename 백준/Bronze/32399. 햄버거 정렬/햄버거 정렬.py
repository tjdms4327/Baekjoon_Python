# bronzeIII_32399
import sys
input = sys.stdin.readline

s = input().strip()
if s == '(1)':
    print(0)
elif s == ')1(':
    print(2)
else:
    print(1)