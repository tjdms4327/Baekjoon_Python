a,b,c=map(int,input().split())
t=int(input())

h=t//(60**2)
m=(t-h*(60**2))//60
s=t-h*(60**2)-m*60
a+=h
b+=m
c+=s

if c>=60:
    mm=c//60
    c=c%60
    b+=mm
    
if b>=60:
    hh=b//60
    b=b%60
    a+=hh

if a>=24:
    a=a%24

print(a,b,c)