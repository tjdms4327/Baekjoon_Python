while True:
    s=input()
    if s=='#': break

    only_alpha=''.join(i for i in s if i.isalpha())
    print(len(set(only_alpha.upper())))