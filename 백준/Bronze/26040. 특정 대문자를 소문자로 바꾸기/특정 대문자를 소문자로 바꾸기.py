s=input()
b=list(input().split())

for i in s:
    if i in b:
        print(i.lower(), end='')
    else:
        print(i, end='')