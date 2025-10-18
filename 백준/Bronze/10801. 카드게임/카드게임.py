# bronzeII_10801
import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = [''] * 10
for i in range(10):
    if A[i] == B[i]:
        result[i] = 'D'
    elif A[i] > B[i]:
        result[i] = 'A'
    else:
        result[i] = 'B'

round_A, round_B = result.count('A'), result.count('B')
if round_A > round_B:
    print('A')
elif round_B > round_A:
    print('B')
else:
    print('D')