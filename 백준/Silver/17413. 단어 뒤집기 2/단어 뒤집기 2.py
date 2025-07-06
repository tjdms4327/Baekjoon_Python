import sys
input=sys.stdin.readline
import re

def reverse_w(s):
    tokens=re.split(r'(<[^<>]*>)',s)
    stack=[]

    for i in tokens:
        if i.startswith('<') and i.endswith('>'):
            stack.append(i)
        else:
            words=i.split(' ')
            stack.append(' '.join(w[::-1] for w in words))
    return ''.join(stack)

s=input().strip()
print(reverse_w(s))