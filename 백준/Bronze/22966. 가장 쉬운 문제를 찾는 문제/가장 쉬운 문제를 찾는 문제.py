n='' ; m=4
for i in range(int(input())):
    a,b=input().split()
    if int(b)<m:
        m=int(b)
        n=a
print(n)