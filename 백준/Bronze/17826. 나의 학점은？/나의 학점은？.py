import sys
input = sys.stdin.readline

scores = list(map(int, input().split()))
hong = int(input())

hong_rank = 1 + sum(1 for x in scores if x > hong)
if hong_rank <= 5:
    print('A+')
elif hong_rank <= 15:
    print('A0')
elif hong_rank <= 30:
    print('B+')
elif hong_rank <= 35:
    print('B0')
elif hong_rank <= 45:
    print('C+')
elif hong_rank <= 48:
    print('C0')
else:
    print('F')