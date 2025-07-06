import sys
input=sys.stdin.readline

n=int(input())
cads=[int(input()) for _ in range(n)]
if cads[0]==max(cads):
    print('S')
else:
    print('N')