# bronzeIII_21185
import sys
input = sys.stdin.readline

n = int(input())

if n%2 == 1:
    print('Either')
elif n%4 == 0:
    print('Even')
else:
    print('Odd')