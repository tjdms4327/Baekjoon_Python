a=list(range(1,101))
n=0
m=input()
b=list(map(int,input().split()))
for j in b:
    if j in a:
        a.remove(j)
    else:
        n+=1

print(n)