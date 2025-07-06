s=input()

set=set()
l=len(s)
for i in range(l):
    for j in range(i, l):
        set.add(s[i:j+1])
print(len(set))