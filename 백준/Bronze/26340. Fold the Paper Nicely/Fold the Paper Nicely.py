n=int(input())
for _ in range(n):
    a,b,c=map(int, input().split())
    sides=[a,b]
    print(f'Data set: {a} {b} {c}')
    #print(sides)
    for i in range(c):
        sides.sort(reverse=True)
        sides[0]//=2
    sides.sort(reverse=True)
    print(*sides, sep=' ')
    print()