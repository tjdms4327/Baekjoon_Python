import sys
input = sys.stdin.readline

roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

n = int(input())
for _ in range(n):
    s = input().strip()
    tot = sum(roman[i] for i in s if i in roman)
    print(tot)