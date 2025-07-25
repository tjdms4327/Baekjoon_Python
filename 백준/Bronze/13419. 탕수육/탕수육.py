n=int(input())
for _ in range(n):
    s=input()
    
    if len(s)%2!=0:
        s*=2
    print(s[::2])
    print(s[1::2])
        