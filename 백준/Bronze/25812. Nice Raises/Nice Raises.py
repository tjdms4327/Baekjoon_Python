# bronzeIII_25812
import sys
input = sys.stdin.readline

n, r = map(int, input().split())
option1, option2 = 0, 0
for _ in range(n):
    salary = int(input())
    if 2*salary < salary + r:
        option1 += 1
    elif 2*salary > salary + r:
        option2 += 1

if option1 == option2:
    print(0)
elif option1 >= n/2:
    print(1)
elif option2 >= n/2:
    print(2)