one=input()
two=input()

for i in range(len(one)):
    prefer=one[i]
    if one[i]<two[i]:
        prefer=two[i]
    print(prefer, end='')