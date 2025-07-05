l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

n=[]
if a%c==0:
    n.append(a//c)
else:
    n.append(a//c+1)
if b%d==0:
    n.append(b//d)
else:
    n.append(b//d+1)
m=max(n)
print(l-m)