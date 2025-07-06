import sys
input=sys.stdin.readline

x=input()
if x.startswith('0x'):
    print(int(x,16))
elif x.startswith('0'):
    print(int(x,8))
else:
    print(x)