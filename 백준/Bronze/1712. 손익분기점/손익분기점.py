a,b,c=map(int, input().split())

if c<=b:
    print(-1)
else:
    n=a/(c-b)
    #print(n)
    print(int(n)+1)