from collections import Counter

n=int(input())
cand={}
for _ in range(n):
    s=input()
    if s[0] in cand:
        cand[s[0]]+=1
    else:
        cand[s[0]]=1
        
found = False
for c in sorted(cand):
    if cand[c] >= 5:
        print(c, end='')
        found = True
if not found:
    print("PREDAJA")