import sys
input = sys.stdin.readline

fibo = [1, 2]
for _ in range(20):
    fibo.append(fibo[-2]+fibo[-1])
fibo.sort(reverse=True)


t = int(input())
for _ in range(t):
    x = int(input())
    
    bx = []
    for f in fibo:
        if x >= f:
            bx.append(1)
            x -= f
        else:
            bx.append(0)
    
    by = bx[:-1]
    fi = fibo[1:]
    result = sum(by[i]*fi[i] for i in range(len(by)))
    print(result)