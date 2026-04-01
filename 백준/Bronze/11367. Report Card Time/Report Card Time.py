n=int(input())
for i in range(n):
    a,b=input().split()
    b=int(b)
    if b>96:
        print(a,'A+')
    elif b>89:
        print(a,'A')
    elif b>86:
        print(a,'B+')
    elif b>79:
        print(a,'B')
    elif b>76:
        print(a,'C+')
    elif b>69:
        print(a,'C')
    elif b>66:
        print(a,'D+')
    elif b>59:
        print(a,'D')
    else:
        print(a,'F')