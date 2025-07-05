def attack(a,b,c,d,i):
    n1, n2=i%(a+b), i%(c+d)
    dog=0
    if n1<=a and n1>0:
        dog+=1
    if n2<=c and n2>0:
        dog+=1
    print(dog)

a,b,c,d=map(int, input().split())
p,m,n=map(int, input().split())

attack(a,b,c,d,p)
attack(a,b,c,d,m)
attack(a,b,c,d,n)