T=int(input())

for i in range(T):
    a,b=input().split()
    a=int(a)
    result=''
    for j in range(len(b)):
        result+=(b[j]*a)

    print(result)