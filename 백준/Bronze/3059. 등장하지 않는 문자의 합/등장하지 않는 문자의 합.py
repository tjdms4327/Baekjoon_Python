import string

T=int(input())

upper=[i for i in string.ascii_uppercase]
for _ in range(T):
    tot=0
    S=list(input())
    for i in upper:
        if i not in S:
            tot+=ord(i)
    print(tot)