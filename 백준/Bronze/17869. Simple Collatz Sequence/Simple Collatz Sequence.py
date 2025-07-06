import sys
input=sys.stdin.readline

def one(n):
    c=0
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n+=1
        c+=1
    return c
        

n=int(input())
c=one(n)
print(c)