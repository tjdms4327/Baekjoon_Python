for i in range(3):
    a=list(map(int,input().split()))
    time=[a[5]-a[2],a[4]-a[1],a[3]-a[0]]
    #print(time)
    for j in range(3):
        if time[j] <0:
            time[j+1]-=1
            time[j]+=60
    time.reverse()
    print(*time, end= ' ')