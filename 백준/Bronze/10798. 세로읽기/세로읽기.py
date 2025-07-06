list1=[[] for _ in range(15)]
for _ in range(5):
    list2=list(input())
    for i in range(len(list2)):
        list1[i].append(list2[i])
list00=sum(list1,[])
print(*list00,sep='')