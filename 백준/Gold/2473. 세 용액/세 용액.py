import sys
input=sys.stdin.readline

n=int(input())
properties=list(map(int, input().split()))
properties.sort()

closest=float('inf')
best=[]

for i in range(n-2):
    left, right =i+1, n-1
    while left<right:
        current=properties[left]+properties[right]+properties[i]
        if abs(current)<abs(closest):
            closest=current
            best = [properties[i], properties[left], properties[right]]
                 
        if current>0:
            right-=1
        elif current<0:
            left+=1
        else:
            break
    if not closest:
        break

print(*best)