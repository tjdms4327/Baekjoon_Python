N, X=map(int,input().split())
price=list(map(int, input().split()))

pay=[]
for i in range(1,N):
    pay.append(price[i-1]+price[i])
print(min(pay)*X)