import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    hp, mp, attack, defense, hp0, mp0, attack0, defense0=map(int, input().strip().split())
    hp+=hp0 ; mp+=mp0 ; attack+=attack0 ; defense+=defense0
    if hp<1: hp=1
    if mp<1: mp=1
    if attack<0: attack=0
    print(hp+5*mp+2*attack+2*defense)