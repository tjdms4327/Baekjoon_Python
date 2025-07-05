import sys
input = sys.stdin.readline

score={}
for i in range(1,9):
    score[i]=int(input())
score=sorted(score.items(), key=lambda x:x[1])

print(sum([x[1] for x in score[3:]]))
idxs=sorted([x[0] for x in score[3:]])
print(*idxs, sep=' ')