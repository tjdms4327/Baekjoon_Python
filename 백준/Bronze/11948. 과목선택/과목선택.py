test=[]
for i in range(6):
    test.append(int(input()))

first=test[:4] ; first.sort()
second=test[4:]
#print(first,first[1:],second)
print(sum(first[1:])+max(second))