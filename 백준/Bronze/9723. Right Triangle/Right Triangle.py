import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    sides = list(map(int, input().split()))
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[-1]**2:
        print(f'Case #{case}: YES')
    else:
        print(f'Case #{case}: NO')