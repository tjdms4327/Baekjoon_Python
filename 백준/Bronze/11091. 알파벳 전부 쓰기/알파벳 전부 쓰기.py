n=int(input())
for _ in range(n):
    s=input().strip().lower()
    filtered=[i for i in s if i.isalpha()]
    set_s=set(filtered)
    
    if len(set_s)==26:
        print('pangram')
    else:
        missing=''.join(i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in filtered)
        print('missing', missing)