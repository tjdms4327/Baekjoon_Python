while True:
    pysical=list(map(float, input().split()))
    if pysical==[0,0,0]: break

    c=0
    if pysical[0]<=4.5 and pysical[1]>=150 and pysical[2]>=200:
        print("Wide Receiver", end=' ') ; c=1
    if pysical[0]<=6 and pysical[1]>=300 and pysical[2]>=500:
        print("Lineman", end=' ') ; c=1
    if pysical[0]<=5 and pysical[1]>=200 and pysical[2]>=300:
        print("Quarterback", end=' ') ; c=1
    if c==0: print("No positions", end=' ')
    print()