n=int(input())
for _ in range(n):
    data, i,j=input().split()
    i,j=int(i),int(j)
    print(data[:i]+data[j:])