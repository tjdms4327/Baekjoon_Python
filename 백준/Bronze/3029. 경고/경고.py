now_list = list(map(int, input().split(':')))
na_list = list(map(int, input().split(':')))

wait=[0,0,0]
now=now_list[0]*3600+now_list[1]*60+now_list[2]
na=na_list[0]*3600+na_list[1]*60+na_list[2]
if na==now:
    wait[0]=24
else:
    if na<now:
        now-=24*3600
    na-=now
    wait=[na//3600, (na%3600)//60, na%60]
print(f"%02d:%02d:%02d"%(wait[0], wait[1], wait[2]))