S=input()
alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a=''
for i in alp:
    if i in S:
        a+=(str(S.index(i))+' ')
    else:
        a+=('-1 ')

print(a[0:-1])