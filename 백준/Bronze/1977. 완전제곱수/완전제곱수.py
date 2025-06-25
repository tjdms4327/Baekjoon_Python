m=int(input())
n=int(input()) 

a=list(range(m,n+1))
r=[]
for i in a:
    ii=int(i**(1/2))
    if i/(ii)==ii:
        #print(i)
        r.append(i)    

if r==[]:
    print(-1)
else:
    print(sum(r))
    print(min(r))