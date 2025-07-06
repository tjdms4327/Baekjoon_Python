n=int(input())
for i in range(n):
    a=list(input().split())
    for j in a:
        print(j[::-1], end=' ')
