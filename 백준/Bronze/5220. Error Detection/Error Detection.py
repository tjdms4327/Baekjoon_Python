import sys
input = sys.stdin.readline

for case in range(int(input())):
    num, check = map(int, input().split())
    n = str(bin(num)).count('1') % 2
    if n == check:
        print("Valid")
    else:
        print("Corrupt")