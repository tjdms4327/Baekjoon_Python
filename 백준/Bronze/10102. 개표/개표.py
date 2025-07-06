v=int(input())
m=input()
a=m.count('A')
b=m.count('B')
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')