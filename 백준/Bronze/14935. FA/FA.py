def fa(x):
    length=len(x)
    while length!=1:
        x=list(length*x[0].split())
    return 'FA'
        
x=list(map(int,input().split()))
print(fa(x))