c=int(input())

for _ in range(c):
    score=list(map(int,input().split()))
    me=sum(score[1:])/score[0]
    num=0
    for i in score[1:]:
        if i >me:
            num+=1
    re=(num/score[0])*100
    print(str(f'{re:.3f}')+'%')