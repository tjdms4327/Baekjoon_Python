import sys
input = sys.stdin.readline

q = int(input())
questions = 0
for _ in range(q):
    xy = list(map(int, input().split()))
    
    if xy[0] == 1:
        questions += xy[-1]
    else: # 입력이 2 y
        if questions < xy[-1]:
            sys.stdin.read()
            print('Adios')
            sys.exit()
        else:
            questions -= xy[-1]
print('See you next month')