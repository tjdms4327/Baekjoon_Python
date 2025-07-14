import sys
input=sys.stdin.readline

name=input().strip()
LOVE=[name.count('L'), name.count('O'), name.count('V'), name.count('E')]
#print(LOVE)

cand_score=0
cand_team=[]
n=int(input().strip())
for _ in range(n):
    team=input().strip()
    team_love=[0, 0, 0, 0]
    for i in range(4):
        team_love[i]=LOVE[i]+team.count('LOVE'[i])
    cand=((team_love[0]+team_love[1])*(team_love[0]+team_love[2])*(team_love[0]+team_love[3])*(team_love[1]+team_love[2])*(team_love[1]+team_love[3])*(team_love[2]+team_love[3]))%100
    #print(team_love, cand)
    if cand>cand_score:
        cand_score=cand
        cand_team=[team]
    elif cand==cand_score:
        cand_team.append(team)
#print(cand_team)
cand_team.sort()
print(cand_team[0])