change={
    'b':'d', 'd':'b',
    'p':'q', 'q':'p'
}

while True:
    s=input().strip()
    if s=='#': break

    y=''
    invalid=False
    for i in s[::-1]:
        if i in change:
            y+=change[i]
        elif i in ['i', 'o', 'v', 'w', 'x']:
            y+=i
        else:
            print('INVALID')
            invalid=True
            break
    if not invalid:
        print(y)