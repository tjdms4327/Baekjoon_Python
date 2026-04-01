import sys
input = sys.stdin.readline

def prime(n):
    res = {1}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    
    res = prime(n)
    tot = sum(res)
    if tot > n:
        ok = True
        for x in res:
            if sum(prime(x)) > x:
                ok = False
                break
        if not ok:
            print('BOJ 2022')
        else:
            print('Good Bye')
    else:
        print('BOJ 2022')