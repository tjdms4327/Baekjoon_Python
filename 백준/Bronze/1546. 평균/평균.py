N=int(input())

scores=list(map(int,input().split()))
avg=sum(scores)/N
x=(avg/max(scores))*100

print(x)