n = int(input())
s = input().strip()

if len(set(s)) >= 3:
    print('Yes')
else:
    print('No')