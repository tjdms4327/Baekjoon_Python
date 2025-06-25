octo={'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    eight=input()
    
    if eight=='#':
        break
        
    num=0
    length=len(eight)-1
    for i in eight:
        num+=(octo[i]*(8**length))
        length-=1
    print(num)