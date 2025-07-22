n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

tot=0
for i in range(n):
    if a[i]>b[i]:
        tot+=3
    elif a[i]==b[i]:
        tot+=1
print(tot)