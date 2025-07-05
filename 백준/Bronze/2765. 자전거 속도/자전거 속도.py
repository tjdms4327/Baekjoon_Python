i=0
while True:
    diameter,turn,time=map(float, input().split())
    if turn==0:
        break
    else:
        i+=1
        diameter_mile=diameter/12/5280
        hour=time/3600
        distance=2*3.1415927*(diameter_mile/2)*turn
        MPH=distance/hour

        print(f'Trip #{i}: {distance:.2f} {MPH:.2f}')