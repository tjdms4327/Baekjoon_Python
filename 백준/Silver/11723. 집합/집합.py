import sys
input=sys.stdin.readline

def cal(x, s):
    if x[-1]!=x[0]:
        x[1]=int(x[1])
    if (x[0]=='add' or x[0]=='toggle') and x[1] not in s:
        s.add(x[1])
    elif (x[0]=='remove' or x[0]=='toggle') and x[1] in s:
        s.remove(x[1])
    elif x[0]=='check':
        if x[1] in s:
            return 1
        else:
            return 0
    elif x[0]=='all':
        s.update(range(1,21))
    elif x[0]=='empty':
        s.clear()

s=set()
m=int(input())
for _ in range(m):
    x=list(input().split())
    result=cal(x,s)
    if result!=None:
        print(result)