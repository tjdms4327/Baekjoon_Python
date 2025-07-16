def card(c):
    n=1
    tot=0
    while tot<c:
        tot+=(1/(n+1))
        n+=1
    return n-1 # 마지막 누적합계(>=c)가 될 때 n에 1이 더해져 있음
    
while True:
    n=float(input())
    if n==0.00: break
    print(f'{card(n)} card(s)')

    
        