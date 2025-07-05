while True:
    s=input()
    if s!='*':
        s_set=set(char for char in s.lower() if char.isalpha())
        if len(s_set)==26:
            print('Y')
        else:
            print('N')
    else:
        break