n=int(input())
for i in range(n):
    a=map(int,input().split())
    b=[]
    for j in a:
        if j%2==0:
            b.append(j)
    print(sum(b),min(b))