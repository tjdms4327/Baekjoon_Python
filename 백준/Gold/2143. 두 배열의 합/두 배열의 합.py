import bisect
import sys
input=sys.stdin.readline

t=int(input())
na=int(input())
a=list(map(int, input().split()))
nb=int(input())
b=list(map(int, input().split()))

sumA=[]
for i in range(na):
    tot=0
    for j in range(i, na):
        tot+=a[j]
        sumA.append(tot)
sumB=[]
for i in range(nb):
    tot=0
    for j in range(i, nb):
        tot+=b[j]
        sumB.append(tot)
sumB.sort()

c=0
for ia in sumA:
    temp=t-ia
    left=bisect.bisect_left(sumB, temp)
    right=bisect.bisect_right(sumB, temp)
    c+=right-left
print(c)