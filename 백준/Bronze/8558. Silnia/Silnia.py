n=int(input())

x=1
for i in range(2, n+1):
    x=(x*i)%10
print(x)