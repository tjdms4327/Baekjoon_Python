def change(s):
    trans={'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    result=[]
    for i in s:
        if i in trans:
            result.append(trans[i])
        else:
            result.append(i)
    return ''.join(result)

s=input().strip()
print(change(s))