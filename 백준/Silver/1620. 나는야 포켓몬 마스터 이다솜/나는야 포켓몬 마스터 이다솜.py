n,m=map(int, input().split())

pocketmon={}
for i in range(n):
    pocketmon[input()]=i+1
pocketmon_name=list(pocketmon.keys())

for _ in range(m):
    i=input()
    try:
        idx=int(i)
        print(pocketmon_name[idx-1])
    except ValueError:
        print(pocketmon[i])
    