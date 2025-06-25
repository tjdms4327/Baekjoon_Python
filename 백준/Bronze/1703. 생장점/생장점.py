while True:
    branchorama=list(map(int, input().split()))
    if branchorama==[0]:
        break
    else:
        a=branchorama[0]
        l=branchorama[1]-branchorama[2]
        for i in range(3,2*a+1,2):
            l*=branchorama[i]
            l-=branchorama[i+1]
    print(l)
            