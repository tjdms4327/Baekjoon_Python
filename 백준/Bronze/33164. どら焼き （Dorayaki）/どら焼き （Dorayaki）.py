n,m=map(int, input().split())
A=list(map(int, input().split())) # n개
B=list(map(int, input().split())) # m개

tot=0
for i in A:
    for j in B:
        tot+=((i+j)*max(i, j))
print(tot)