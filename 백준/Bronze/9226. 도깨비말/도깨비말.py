vowels = set('aeiou')
while True:
    s=input()
    if s=='#': break

    if s[0] in vowels: print(s+'ay')
    elif not any(i in vowels for i in s): print(s+'ay')
    else:
        fig, rest='', ''
        for i in range(len(s)):
            if s[i] in vowels:
                fig+=s[i:]
                break
            else:
                rest+=s[i]
        print(fig+rest+'ay')