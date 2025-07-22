n, l=map(int, input().split())

best, cnt=0,0
for _ in range(n):
    s=input()
    black, pre=0, '0'
    for i in s:
        if i=='1' and pre=='0':
            black+=1
        pre=i
        
    if black>best: 
        best=black
        cnt=1
    elif black==best:
        cnt+=1
print(best, cnt)