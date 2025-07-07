weigh=[13,7,5,3,3,2]

first=list(map(int, input().split()))
second=list(map(int, input().split()))

diff=[(first[i]-second[i])*weigh[i] for i in range(6)]
score=sum(diff)-1.5
if score>0:
    print('cocjr0208')
else:
    print('ekwoo')