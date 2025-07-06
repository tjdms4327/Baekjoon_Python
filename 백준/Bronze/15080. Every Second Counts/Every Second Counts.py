def to_second(time):
    return time[0]*3600+time[1]*60+time[2]

depart=list(map(int, input().split(' : ')))
arrive=list(map(int, input().split(' : ')))

time = to_second(arrive) - to_second(depart)
if time<0:
    time+=24*3600
print(time)