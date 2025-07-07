YMD=list(map(int,input().split('-')))

result='TOO LATE'
if (YMD[0]<=2023):
    if (YMD[1]==9) and (YMD[2]<=30-(35-21)):
        result='GOOD'
    elif YMD[1]<=8:
        result='GOOD'
print(result)