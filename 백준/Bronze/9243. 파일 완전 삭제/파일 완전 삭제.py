n=int(input())
before=input()
after=input()

if n%2==0 and before==after:
    print('Deletion succeeded')
elif n%2==1:
    answer=''.join('1' if i=='0' else '0' for i in before)
    if answer==after:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    print('Deletion failed')