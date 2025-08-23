import sys 
input = sys.stdin.readline

n = int(input())
first = int(input())

first_0 = [1, 0, 1, 0, 1]
first_1 = [0, 1, 0, 1, 0]
if n >= 6:
    print("Love is open door")
else:
    if first == 0:
        print(*first_0[:n-1], sep='\n')
    else:
        print(*first_1[:n-1], sep='\n')
            