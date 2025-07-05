while True:
    start, wd, inout=input().split()
    start, inout=int(start), int(inout)
    
    if start==0 and inout==0 and wd=='W':
        break
    else:
        if wd=='W':
            if start-inout>=-200:
                print(start-inout)
            else:
                print('Not allowed')
        else:
            print(start+inout)