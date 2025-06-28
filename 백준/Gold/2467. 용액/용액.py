import sys
input=sys.stdin.readline

n=int(input())
properties=list(map(int, input().split()))

left, right=0, n-1
best=(properties[left], properties[right])
best_tot=float('inf')
while left<right:
    tot=properties[left]+properties[right]
    if abs(tot)<abs(best_tot):
        best_tot=tot
        best = (properties[left], properties[right])
    if tot==0:
        break
    elif tot>0:
        right-=1
    else:
        left+=1

print(best[0], best[1])