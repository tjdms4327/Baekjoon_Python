import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n, s=input().strip().split()
    n=int(n) ; s=ord(s)

    for i in range(1, n+1):
        if s>90:
            s=ord('A')
        print(chr(s)*i)
        s+=1
    print()