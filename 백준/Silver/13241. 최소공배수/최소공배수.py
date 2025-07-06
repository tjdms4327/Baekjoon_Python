def mul(a,b):
    x,y=min(a,b), max(a,b)
    result=1
    for i in range(x, 1,-1):
        if y%i==0 and x%i==0:
            result*=i
            x=x//i
            y//=i
        if y<i:
            break
    return result*x*y
    
a,b=map(int, input().split())
result=mul(a,b)
print(result)