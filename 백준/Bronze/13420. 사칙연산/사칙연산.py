def compute(a, E, b):
    a=int(a) ; b=int(b)
    if E=='+': return a+b
    elif E=='-': return a-b    
    elif E=='*': return a*b    
    elif E=='/': return a/b    

n=int(input())
for _ in range(n):
    s=input().split()
    
    result=compute(s[0], s[1], s[2])
    if result==int(s[-1]):
        print('correct')
    else:
        print('wrong answer')