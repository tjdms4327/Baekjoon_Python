n=0 ;c=0 ;d=0
for i in range(4):
    a,b=map(int,input().split())
    c=b-a
    d+=c
    if d>n:
        n=d
print(n)