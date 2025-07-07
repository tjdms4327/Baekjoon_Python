n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

really=0
for i in range(n):
    if a[i]<=b[i]:
        really+=1
print(really)