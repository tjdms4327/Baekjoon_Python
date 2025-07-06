n=int(input())
while n != -1:
    a=[] ;b=''
    for i in range(1,n):
        if n%i==0:
            a.append(i)
            b+=(str(i) +' + ')
    total=sum(a)
    b=b[0:-2]
    if total== n:
        print(n,'=',b)
    else:
        print(n,'is NOT perfect.')
    n=int(input())