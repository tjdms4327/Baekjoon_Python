t=int(input())
for _ in range(t):
    a, b=input().split()
    
    print('Distances:', end=' ')
    distances=[]
    for i in range(len(a)):
        dis=(ord(b[i])-ord(a[i])+26)%26
        distances.append(dis)
    print(*distances, sep=' ')