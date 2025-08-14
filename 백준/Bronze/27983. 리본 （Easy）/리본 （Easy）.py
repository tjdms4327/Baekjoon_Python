import sys
input=sys.stdin.readline

n=int(input())
x=list(map(int, input().split()))
l=list(map(int, input().split()))
c=list(input().split())


for i in range(n):
    for j in range(i+1, n):
        if c[i]!=c[j]:
            if abs(x[i]-x[j])<=l[i]+l[j] :
                print('YES')
                print(i+1, j+1)
                exit(0)
print('NO')