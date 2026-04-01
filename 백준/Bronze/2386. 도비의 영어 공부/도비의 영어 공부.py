while True:
    s=input()
    
    if s=='#':
        break
    c=s[0]
    s=s[1:].lower()
    print(c, s.count(c))