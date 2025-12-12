import sys
input = sys.stdin.readline

a, b = map(int, input().split())

e = a+1
while e <= 62:
    if str(2**e)[0] == str(b):
        print(e)
        sys.exit()
    else:
        e += 1

print(0)