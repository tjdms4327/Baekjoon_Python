n,k=map(int,input().split())
a1=1;a2=1;a3=1
for i in range(2,n+1):
    a1=a1*i
for j in range(2,n-k+1):
    a2=a2*j
for k in range(2,k+1):
    a3=a3*k
print(int(a1/(a2*a3)))