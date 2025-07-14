import sys
input=sys.stdin.readline

def head(h): 
    left=h
    s=input().strip()
    for j in s:
        if left==0: continue
        if j=='c': left+=1
        elif j=='b': left-=1

    return left

t=int(input().strip())
for i in range(1, t+1):
    h=int(input().strip())
    result=head(h)
    print(f'Data Set {i}:\n{result}\n')