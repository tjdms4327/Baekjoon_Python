import sys
input=sys.stdin.readline

result=[]
t=int(input())
for _ in range(t):
    x=int(input())
    result.append(str(2*x-1))
print('\n'.join(result))