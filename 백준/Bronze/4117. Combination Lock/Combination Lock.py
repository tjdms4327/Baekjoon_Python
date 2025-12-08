import sys
input = sys.stdin.readline

while True:
    n, t1, t2, t3 = map(int, input().split())
    if n==t1==t2==t3==0:
        break
    
    a = (t2-t1) % n
    b = (t2-t3) % n
    ans = 4*n - 1 + a + b
    print(ans)
