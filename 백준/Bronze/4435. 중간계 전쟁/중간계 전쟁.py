n=int(input())

for i in range(1,n+1):
    g=list(map(int, input().split()))
    s=list(map(int, input().split()))

    good=g[0]+g[1]*2+g[2]*3+g[3]*3+g[4]*4 +g[5]*10
    evil=s[0]+s[1]*2+s[2]*2+s[3]*2+s[4]*3+s[5]*5+s[6]*10
    if good>evil:
        print(f"Battle {i}: Good triumphs over Evil")
    elif good==evil:
        print(f"Battle {i}: No victor on this battle field")
    else:
        print(f"Battle {i}: Evil eradicates all trace of Good")