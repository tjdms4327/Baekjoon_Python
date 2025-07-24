def compare(s):
    a, E, b=s
    a=int(a) ; b=int(b)
    if E=='>': return a>b
    elif E=='>=': return a>=b
    elif E=='<': return a<b
    elif E=='<=': return a<=b
    elif E=='==': return a==b
    elif E=='!=': return a!=b

i=0
while True:
    s=input().split()
    if 'E' in s: break

    i+=1
    result=compare(s)
    print(f'Case {i}: {str(result).lower()}')