n=int(input())
for _ in range(n):
    PF='FAIL'
    examinee,s,m,t=map(int, input().split())
    if (s+m+t>=55) and (s>=35*0.3 and m>=25*0.3 and t>=40*0.3):
        PF='PASS'
    print(examinee, s+m+t, PF)