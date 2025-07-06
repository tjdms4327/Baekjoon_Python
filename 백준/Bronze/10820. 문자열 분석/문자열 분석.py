import sys
input=sys.stdin.readline

while True:
    try:
        s=input()
        if not s:
            break
            
        chars=[0,0,0,0]
        for char in s:
            if char=='\n': pass
            elif char.islower(): chars[0]+=1
            elif char.isupper(): chars[1]+=1
            elif char.isdigit(): chars[2]+=1
            elif char.isspace(): chars[3]+=1
        print(*chars)

    except EOFError:
        break