import sys
input = sys.stdin.readline

while True:
    n, l, r = map(int, input().split())
    if n==l==r==0:
        break
    
    A = [int(input()) for _ in range(n)]
    
    count = 0
    for x in range(l, r+1):
        div = False
        for i in range(n):
            if x%A[i]==0:
                div = True
                if (i+1)%2==1:
                    count += 1
                break
        if not div:
            if n%2 == 0:
                count += 1
    print(count)
                