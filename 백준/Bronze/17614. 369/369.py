import sys
input=sys.stdin.readline

n=int(input())
s=0
for i in range(1,n+1):
    s+= str(i).count('3')+str(i).count('6')+str(i).count('9')
print(s) 