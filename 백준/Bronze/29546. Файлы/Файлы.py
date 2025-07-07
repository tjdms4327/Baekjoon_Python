n=int(input())
files=[None]
files.extend([input() for _ in range(n)])
m=int(input())
for _ in range(m):
    f,l=map(int, input().split())
    i=f
    while i<=l:
        print(files[i])
        i+=1