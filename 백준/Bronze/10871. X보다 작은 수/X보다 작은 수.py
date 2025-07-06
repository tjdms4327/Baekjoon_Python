import sys
N,X=map(int,sys.stdin.readline().split())
A=map(int,sys.stdin.readline().split())

a=''
for i in A:
    if i<X:
        a+=(' '+str(i))
print(a.lstrip())