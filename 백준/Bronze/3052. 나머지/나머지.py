x=[]
for i in range(10):
    a=int(input())
    b=a%42
    if b not in x:
        x.append(b)
    else:
        pass
print(len(x))