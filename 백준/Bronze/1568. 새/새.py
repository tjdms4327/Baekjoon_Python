n=int(input())

time=0
k=1
while k<=n:
    time+=1
    n-=k
    k+=1
    if n<k:
        k=1
print(time)