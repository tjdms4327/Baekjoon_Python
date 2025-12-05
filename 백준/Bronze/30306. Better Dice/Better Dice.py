import sys
input = sys.stdin.readline

n = int(input())
D1 = list(map(int, input().split()))
D1.sort()
D2 = list(map(int, input().split()))
D2.sort()

first, second = 0, 0
for d1 in D1:
    for d2 in D2:
        if d1 > d2: 
            first += 1
        elif d1 < d2:
            second += 1

if first > second:
    print('first')
elif second > first:
    print('second')
else:
    print('tie')