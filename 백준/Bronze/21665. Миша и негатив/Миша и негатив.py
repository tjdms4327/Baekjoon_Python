n,m=map(int, input().split())

standard=[]
for _ in range(n):
    standard.append(list(input()))

x=input()
count=0
for i in range(n):
    actual=input()
    for j in range(m):
        if standard[i][j] == actual[j]:
            count+=1
print(count)