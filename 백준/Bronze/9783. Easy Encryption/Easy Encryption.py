import sys
input = sys.stdin.readline

s = input().strip()
for i in s:
    if i.isupper():
        print(f'{ord(i)-ord("A")+27:02d}', end = '')
    elif i.islower():
        print(f'{ord(i)-ord("a")+1:02d}', end = '')
    elif i.isdigit():
        print(f'#{i}', end = '')
    else: 
        print(i, end = '')