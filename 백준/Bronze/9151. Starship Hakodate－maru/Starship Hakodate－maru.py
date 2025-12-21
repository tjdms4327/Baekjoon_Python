import sys
input = sys.stdin.readline

while True:   
    n = int(input())
    if n==0:
        break
    
    best = 0
    i = 0
    while True:
        temp = i*(i+1)*(i+2)//6
        if temp > n:
            break

        k = int((n - temp) ** (1/3))
        while (k+1)**3 <= n - temp:
            k += 1
        while k**3 > n - temp:
            k -= 1
        
        best = max(best, temp + k**3)
        i += 1

    print(best)