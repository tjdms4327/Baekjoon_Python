T=int(input())
for _ in range(T):
    N=int(input())
    totC, GPA=0,0
    for _ in range(N):
        C,G=map(float, input().split())
        totC+=C
        GPA+=(G*C)
    GPA/=totC
    print(int(totC), "{:.1f}".format(GPA))