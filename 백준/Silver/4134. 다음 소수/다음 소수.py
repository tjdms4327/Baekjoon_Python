def prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True
            

n=int(input())
for _ in range(n):
    x=int(input())
    while True:
        if prime(x):
            print(x)
            break
        x+=1