k=int(input())
n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

cnt=0
for i in A:
    for j in B:
        if i+k==j:
            cnt+=1
print(cnt)