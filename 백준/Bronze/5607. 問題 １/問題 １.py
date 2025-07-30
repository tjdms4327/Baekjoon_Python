n=int(input())

A, B=0,0
for _ in range(n):
    a, b=map(int, input().split())

    tot=a+b
    if a>b: A+=tot
    elif a<b: B+=tot
    else: A+=a ; B+=b

print(A, B)