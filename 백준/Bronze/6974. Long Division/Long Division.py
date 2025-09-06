import sys
input = sys.stdin.readline

for case in range(int(input())):
    dividend = int(input())
    divisor = int(input())

    print(dividend // divisor)
    print(dividend % divisor)
    print()