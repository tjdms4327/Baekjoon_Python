n=int(input())

a=[]
for i in range(n//5+1):
    k=0
    k+=i
    m=n-(5*i)
    if m%3==0:
        k+=(m//3)
        a.append(k)
if len(a)==0:
    print(-1)
else:
    print(sorted(a)[0])
        