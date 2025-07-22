def fee(c, d):
    ParsTel=c*30 + d*40
    ParsCell=c*35 + d*30
    ParsPhone=c*40 + d*20
    return min(ParsTel, ParsCell, ParsPhone)


while True:
    c, d=map(int, input().split())
    if c==d==0: break

    print(fee(c, d))