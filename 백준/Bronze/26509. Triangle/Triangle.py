# bronzeIII_26509
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for _ in range(n):
    triangle1 = list(map(int, input().split()))
    triangle2 = list(map(int, input().split()))
    
    triangle1.sort(); triangle2.sort()
    if (triangle1[0]**2 + triangle1[1]**2 == triangle1[2]**2)\
        and (triangle1 == triangle2):
            print('YES\n')
    else:
        print('NO\n')