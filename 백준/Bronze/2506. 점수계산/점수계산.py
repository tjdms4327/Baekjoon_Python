n=int(input())
ox=list(map(int, input().split()))

score=ox[0]
num=1
for i in range(1, n):
    if ox[i]==1 :
        if ox[i-1]==1:
            num+=1
        else:
            num=1
        score+=num
print(score)