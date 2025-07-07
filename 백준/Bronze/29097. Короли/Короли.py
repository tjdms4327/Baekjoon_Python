n,m,k,a,b,c=map(int, input().split())
soldiers=[n*a, m*b, k*c]
kings=['Joffrey', 'Robb', 'Stannis']

maximum=max(soldiers)
for i in range(3):
    if maximum==soldiers[i]:
        print(kings[i], end=' ')
