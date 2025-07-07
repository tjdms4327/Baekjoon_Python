n=int(input())
rain=list(map(int, input().split()))

anger,gauge=0,0
for r in rain:
    if r==1:
        anger+=1
    else:
        anger-=1
    gauge+=anger
print(gauge)