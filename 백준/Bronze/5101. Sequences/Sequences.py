while True:
    start, diff, target=map(int, input().split())
    if start==diff==target==0: break

    if diff!=0 and (target-start)%diff==0 and (target-start)//diff>=0:
            print((target-start)//diff +1) # start가 첫번째 행이니까
    else:
        print('X')