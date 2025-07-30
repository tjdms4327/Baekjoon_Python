n=int(input())
A=list(input())

for i in range(1, n):
    if A[i-1]==A[i]:
        A[i-1]=A[i-1].upper()
        A[i]=A[i].upper()
print(*A, sep='')