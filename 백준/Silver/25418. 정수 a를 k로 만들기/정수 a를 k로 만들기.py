import sys
input=sys.stdin.readline

a, k=map(int, input().split())

cnt=0
while k>a:
    if k%2==0 and k//2>=a:
        k//=2
    else:
        k-=1
    cnt+=1
print(cnt)