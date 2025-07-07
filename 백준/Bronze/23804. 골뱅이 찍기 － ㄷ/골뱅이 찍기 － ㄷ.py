n=int(input())

for i in range(n*5):
    if (i >=n*4) or (i<n):
        print('@'*n*5)
    else:
        print('@'*n)