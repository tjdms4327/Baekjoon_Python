n=int(input())
while n!=0:
    levs=[int(input()) for _ in range(n)]
    levs.reverse()
    print(*levs, sep='\n')
    print(0)
    n=int(input())