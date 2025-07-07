import sys
input = sys.stdin.readline

n=int(input())
s=input()
box, c=1,0
for i in s:
    if i=='R':
        if box<3:
            box+=1
    else:
        if box>1:
            box-=1
    if box==3:
        c+=1
print(c)