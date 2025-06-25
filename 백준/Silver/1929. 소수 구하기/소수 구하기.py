def prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True
            

a,b=map(int,input().split())
while a<=b:
    if prime(a):
        print(a)
    a+=1