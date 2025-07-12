import sys
input=sys.stdin.readline

mushrooms=[int(input().strip()) for i in range(10)]
scores=[0]*(11)
for i in range(10):
    scores[i+1]=scores[i]+mushrooms[i]

cand=0
diff=float('inf')
for i in scores:
    if abs(100-i)<=diff: # diff가 같으면 더 큰 값 선택
        cand=i
        diff=abs(100-i)
print(cand)
        