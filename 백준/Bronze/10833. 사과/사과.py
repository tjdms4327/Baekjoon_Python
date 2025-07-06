n=0
for i in range(int(input())):
    a,b=map(int,input().split())
    n+=(b%a)
print(n)