t=int(input())
for _ in range(t):
    x=int(input())
    bi_x=list(reversed(bin(x)[2:]))
    #print(bi_x)
    result=list(filter(lambda x: bi_x[x]=='1', range(len(bi_x))))
    print(*result)