x=[] ;y=[]

for i in range(3):
    a,b=map(int,input().split())
    x.append(a) ; y.append(b)
x0=sum(list(set(x)))*2
y0=sum(list(set(y)))*2
print(x0-sum(x),y0-sum(y))