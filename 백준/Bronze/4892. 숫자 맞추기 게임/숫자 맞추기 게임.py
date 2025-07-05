n=int(input())
i=1
while (n!= 0):
    n1=n*3
    if (n1%2==0):
        n2=n1/2
        print('%d. even' % i, end= ' ')
    else:
        n2=(n1+1)/2
        print('%d. odd' % i, end= ' ')
    n3=3*n2
    n4=n3/9
    print("%d" % n4)
    n=int(input())
    i+=1