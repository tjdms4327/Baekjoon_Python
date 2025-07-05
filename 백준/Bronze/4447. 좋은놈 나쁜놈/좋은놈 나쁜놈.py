n=int(input())
for _ in range(n):
    default='GOOD'
    name=input()
    s=name.lower()
    b=s.count('b')
    g=s.count('g')
    if b>g:
        default='A BADDY'
    elif b==g:
        default='NEUTRAL'

    print(f'{name} is {default}')
        