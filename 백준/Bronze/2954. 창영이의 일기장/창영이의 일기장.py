s=input()

i=0
while i<len(s):
    if s[i] not in ['a', 'e', 'i', 'o', 'u']:
        print(s[i], end='')
        i+=1
    else:
        print(s[i], end='')
        i+=3