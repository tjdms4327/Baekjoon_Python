import sys
input=sys.stdin.readline

height=0
while True:
    line=input().strip()
    if not line:
        break
    s,x=line.split()
    if s=='Stair':
        height+=int(x)*17
    else:
        height+=int(x)*21
print(height)
