import sys
input=sys.stdin.readline

counter={}
n=int(input())
for _ in range(n):
    i=int(input())
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1
sort_c=sorted(counter.items(), key=lambda x: (-x[1],x[0]))
print(sort_c[0][0])