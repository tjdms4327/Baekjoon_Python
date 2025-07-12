import sys
input=sys.stdin.readline

def C(n):
    c=[n]
    while c[-1]!=1:
        if c[-1]%2==0: c.append(c[-1]//2)
        else: c.append(3*c[-1]+1)
    return len(c)
    
n=int(input().strip())
result=C(n)
print(result)