import sys
N=int(sys.stdin.readline())

result=[]
for i in range(N):
    a=int(sys.stdin.readline())
    result.append(a)

for j in sorted(result):
    print(j)