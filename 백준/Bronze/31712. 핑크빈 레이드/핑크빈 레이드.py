import sys
input=sys.stdin.readline

cu, du=map(int, input().split())
cd, dd=map(int, input().split())
cp, dp=map(int, input().split())
h=int(input())

time=0
h-=(du+dd+dp) # 0초에서 공격 있음
if h<=0: 
    print(0); exit(0)
while h>0:
    next_attack = min(
        cu - (time % cu) if time % cu != 0 else cu,
        cd - (time % cd) if time % cd != 0 else cd,
        cp - (time % cp) if time % cp != 0 else cp
    )
    time += next_attack

    if time % cu == 0:
        h -= du
    if time % cd == 0:
        h -= dd
    if time % cp == 0:
        h -= dp
print(time)
    