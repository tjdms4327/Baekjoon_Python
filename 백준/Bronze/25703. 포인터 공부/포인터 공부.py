import sys
input = sys.stdin.readline

n = int(input())


print('int a;')
past, cur, star = 'a', 'ptr', '*'
for i in range(1, n+1):
    print(f'int {star}{cur} = &{past};')
    past = cur
    cur = 'ptr' + str(i+1)
    star = '*'*(i+1)