n=int(input())
i=1
while (n-i)>0:
    n-=i
    i+=1

if i%2==0:
    a=1
    b=i
    for _ in range(n-1):
        a+=1
        b-=1
else:
    a=i
    b=1
    for _ in range(n-1):
        a-=1
        b+=1
print("%d/%d\n" % (a,b))