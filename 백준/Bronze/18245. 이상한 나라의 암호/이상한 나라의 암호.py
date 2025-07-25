i=0
while True:
    s=input()
    if s=='Was it a cat I saw?': break

    i+=1
    for x in s[::i+1]:
        print(x, end='')
    print()