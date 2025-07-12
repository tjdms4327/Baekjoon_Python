import sys
input=sys.stdin.readline

num=list(input().strip())
idx=num.index('*')
for i in range(10):
    n=num[:] # 복사
    n[idx]=str(i)
    for j in range(12): # 체크기호 제외하고 
        if j%2==0: n[j]=int(n[j])
        else: n[j]=3*int(n[j])
    tot=sum(n[:-1])

    m=int(num[-1])
    if m==0:
        if tot%10==0: print(i) ; sys.exit()
        else: continue
    else:
        cand=10-tot%10
        if cand==m: print(i) ; sys.exit()
        else: continue
        