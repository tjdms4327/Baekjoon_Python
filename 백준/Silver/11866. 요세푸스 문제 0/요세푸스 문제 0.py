n, k=map(int, input().split())

people=[i for i in range(1, n+1)]
idx=0
print('<', end='')
while people:
    idx=(idx + k-1)%len(people)
    print(people.pop(idx), end='')

    if people:
        print(',', end=' ')
    else:
        pass
        
print('>')