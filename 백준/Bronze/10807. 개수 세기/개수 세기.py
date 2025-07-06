N=int(input())
a=[]
a=input().split()
v=input()

b=0
for i in range(N):
    if v == a[i]:
        b+=1
    else:
        pass

print(b)