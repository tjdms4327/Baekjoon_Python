n=int(input())
sort=list(map(int, input().split()))

line=[0 for _ in range(n)]
k=1
for i in sort:
    if line[i]!=0:
        for j in range(n-1,i,-1):
            line[j]=line[j-1]
    line[i]=k
    k+=1

line.reverse()
print(*line, sep=' ')