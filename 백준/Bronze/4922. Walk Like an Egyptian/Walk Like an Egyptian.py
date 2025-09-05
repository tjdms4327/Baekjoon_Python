import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break

    tot = (n-1) ** 2 + n
    print(f'{n} => {tot}')