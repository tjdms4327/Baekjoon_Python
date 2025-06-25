n=int(input())
a=map(int,input().split())

x=0
for i in a:
    if a != 1:
        l=[]
        for j in range(1,i):
            if i%j==0:
                l.append(j)
        if len(l)==1:
            x+=1
print(x)