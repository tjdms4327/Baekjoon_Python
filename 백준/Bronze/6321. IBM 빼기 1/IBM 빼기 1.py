import sys
input=sys.stdin.readline

t=int(input().strip())
for j in range(t):
    s=list(input().strip())
    print(f'String #{j+1}')
    for i in s:
        if i=='Z': print('A', end='')
        else:
            ord_i=ord(i)+1
            print(chr(ord_i), end='')
    print()
    print()
    