import sys
input=sys.stdin.readline

n=int(input().strip())
milk_shop=list(map(int, input().strip().split()))

milk=-1
cnt=0
for i in milk_shop:
    if ((milk==-1 or milk==2) and i==0) or (milk==0 and i==1) or (milk==1 and i==2):
        cnt+=1
        milk=i
print(cnt)        