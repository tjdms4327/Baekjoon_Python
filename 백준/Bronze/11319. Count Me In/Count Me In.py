n=int(input())

for i in range(n):
    m=input().lower()
    a=0 ; b=0
    for j in m:
        if j == ' ':
            pass
        elif j in ['a','e','i','o','u']:
            b+=1
        else:
            a+=1
    print(a,b)