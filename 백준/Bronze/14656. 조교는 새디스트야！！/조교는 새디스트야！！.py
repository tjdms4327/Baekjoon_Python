import sys
input=sys.stdin.readline

n=int(input())
students=list(map(int, input().split()))
err=0
for i in range(n):
    if i+1 != students[i]:
        err+=1
        #print(i, students[i])
print(err)