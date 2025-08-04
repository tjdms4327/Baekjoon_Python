import sys
input=sys.stdin.readline

a, b, c=map(int, input().split())



day=0
while c>0:
    c-=a
    day+=1

    if day%7==0: 
        c-=b
print(day)