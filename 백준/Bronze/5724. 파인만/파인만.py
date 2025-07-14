while True:
    n=int(input())
    if n==0: break

    square=0    
    for i in range(1, n+1):
        temp=n-i+1
        square+=(temp**2)
    print(square)