import sys
input = sys.stdin.readline

n = int(input())

i = 1
puang = False

while True:
    n -= i
    i += 1
    puang = not puang
    
    if n<0:
        if puang:
            print(abs(n))
        else:
            print(0)
        break