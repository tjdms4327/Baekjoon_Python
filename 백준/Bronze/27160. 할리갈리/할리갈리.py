import sys
input=sys.stdin.readline

n=int(input().strip())
ring={'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}
for _ in range(n):
    fruit, i=input().strip().split()
    i=int(i)
    ring[fruit]+=i
    
if 5 in ring.values(): 
    print('YES')
else: print('NO')