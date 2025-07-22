from math import ceil

n=int(input())
i=0
be, al=0,0
while n!=0:
    current=ceil(n/2)
    if i%2==0:
        be+=current
    else:
        al+=current
    i+=1
    n-=current
print(al, be)