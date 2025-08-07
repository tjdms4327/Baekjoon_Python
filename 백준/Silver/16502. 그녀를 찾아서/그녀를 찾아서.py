import sys
input=sys.stdin.readline

time=int(input())
m=int(input())



mapping={'A':0, 'B':1, 'C':2, 'D':3}
transition = [[0.0]*4 for _ in range(4)]

for _ in range(m):
    start, end, percent=input().split()
    transition[mapping[start]][mapping[end]]=float(percent)

prob=[.25, .25, .25, .25]
for _ in range(time):
    next_prob=[0.0]*4
    for cur in range(4): 
        for next in range(4):
            next_prob[next]+=prob[cur]*transition[cur][next]
    prob=next_prob

for p in prob:
    print(f"{p*100:.2f}")