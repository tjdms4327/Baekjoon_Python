n=int(input())
interest=input()

b=interest.count('B')
s=interest.count('S')
a=interest.count('A')
if b==s==a:
    print('SCU')
else:
    most=max(b, s, a)
    if b==most: print('B', end='')
    if s==most: print('S', end='')
    if a==most: print('A', end='')