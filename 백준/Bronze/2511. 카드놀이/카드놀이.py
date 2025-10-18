# bronzeII_2511
import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

score_A, score_B = 0, 0
result = [''] * 10
for i in range(10):
    if A[i] == B[i]:
        result[i] = 'D'
    elif A[i] > B[i]:
        result[i] = 'A'
    else:
        result[i] = 'B'

score_A = result.count('A') * 3 + result.count('D')
score_B = result.count('B') * 3 + result.count('D')
print(score_A, score_B)

if score_A > score_B:
    print('A')
elif score_B > score_A:
    print('B')
else:
    if 'A' in result or 'B' in result:
        for r in reversed(result):
            if r == 'A':
                print('A')
                exit()
            elif r == 'B':
                print('B')
                exit()
    else:
        print('D')