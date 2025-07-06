n=int(input())

members=[]
for _ in range(n):
    age, name=input().split()
    members.append([int(age), name])
    
sort_member=sorted(members, key=lambda x:x[0])
for i in sort_member:
    print(*i, sep=' ')