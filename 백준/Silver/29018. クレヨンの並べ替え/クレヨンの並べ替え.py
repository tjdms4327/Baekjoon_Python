import sys
input = sys.stdin.readline

while True:  
    s = input().strip()
    if s == '#':
        break
    
    lowercase = []
    uppercase = []
    digits = []
    for x in s:
        if x.islower():
            lowercase.append(x)
        elif x.isupper():
            uppercase.append(x)
        else:
            digits.append(x)
    
    result = sorted(lowercase)+sorted(uppercase)+sorted(digits)
    print(''.join(result))