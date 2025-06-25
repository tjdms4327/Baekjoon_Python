while True:
    n=input()
    if n=='0':
        break
    else:
        zero=n.count('0')
        one=n.count('1')
        print(len(n)+1 + zero*4 + one*2 + (len(n)-zero-one)*3)