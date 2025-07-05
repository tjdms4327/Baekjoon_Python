t=int(input())
for _ in range(t):
    num=int(input())
    print("Pairs for %d: " % num, end='')
    min=1
    max=num-1
    while (min<max):
        if min == 1:
            print(min, max, end='')
        else:
            print(',', min, max, end='')
        min+=1
        max-=1
    print()