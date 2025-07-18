while True:
    tot, not_bed=map(int, input().split())
    if tot==not_bed==0: break

    bed=tot-not_bed
    if bed%2==0:
        print(bed//2, 0)
    else: 
        if bed>=3:
            print((bed-3)//2, 1)
        else: print(0,0) # bed==2는 이미 위에서 처리됨