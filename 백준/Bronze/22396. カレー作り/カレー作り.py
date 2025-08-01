while True:
    r0, w0, c, r=map(int, input().split())
    if r0+w0+c+r==0: break 

    x=0
    while True:
        tot_r=r0+x*r
        tot_require=c*w0

        if tot_r>=tot_require:
            print(x)
            break
        x+=1