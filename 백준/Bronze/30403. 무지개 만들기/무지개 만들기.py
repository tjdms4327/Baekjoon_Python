n = int(input())
s = input().strip()

rainbow_small = set('roygbiv')
rainbow_big = set('ROYGBIV')

small = rainbow_small.issubset(set(s))
big = rainbow_big.issubset(set(s))
if small and big:
    print('YeS')
elif small:
    print('yes')
elif big:
    print('YES')
else:
    print('NO!')
