import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    print(f'Data Set {case}:')

    e, a = map(int, input().split())
    prop = e / a
    if e <= a: 
        print('no drought\n')
    else:
        while prop > 5:
            print('mega', end = ' ')
            prop /= 5
        print('drought\n')
        