from collections import Counter

n=int(input())
sang=list(input().split())

m=int(input())
nums=list(input().split())

x=Counter(sang)
#print(x)
for i in nums:
    if i in x.keys():
        print(x[i], end=' ')
    else:
        print(0, end=' ')