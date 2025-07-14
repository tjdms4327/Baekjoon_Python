import sys
input=sys.stdin.readline

n=int(input().strip())
cand, score=[], 0
for _ in range(n):
    a,b=input().strip().split()
    b=int(b)
    if b>score:
        cand=[a]
        score=b
    elif b==score:
        cand.append(a)
    #print(cand, score)
cand.sort()
print(cand[0])