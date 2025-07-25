t=int(input())
for _ in range(t):
    s=input()

    A, B=s[0], s[-1]
    format=A+A+B+B+A+B+B
    like=0
    if len(s)==7 and len(set(s))==2 and s==format:
        like=1
    print(like)