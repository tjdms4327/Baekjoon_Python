import sys
input=sys.stdin.readline

x=int(input())
shoot=int(input())
faul=int(input())



score=0
if shoot==1: 
    score+=x

if faul==1: # 파울
    if shoot==1: # 슛 성공
        new=int(input())
        if new==1: 
            score+=1
    else:
        new=[int(input()) for _ in range(x)]
        score+=sum(new)
print(score)