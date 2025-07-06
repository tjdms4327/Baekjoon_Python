n=int(input())
a=list(map(int,input().split()))
sum_a=sum(a)
b,c=map(int,input().split())

n=0
for i in a:
    d=i-b
    n+=1
    if d>0:
        if d%c==0:
            n+=(d//c)
        else:
            n+=((d//c)+1)
print(n)