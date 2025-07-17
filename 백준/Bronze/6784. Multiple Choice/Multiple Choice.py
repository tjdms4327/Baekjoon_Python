n=int(input())

cnt=0
students=[input() for _ in range(n)]
for i in range(n):
    if students[i]==input():
        cnt+=1
print(cnt)