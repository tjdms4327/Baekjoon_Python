import sys 
input = sys.stdin.readline

from collections import Counter

n = int(input())
vote = list(map(int, input().split()))


counter = Counter(vote)
if counter[0] >= n/2:
    print('INVALID')
elif counter[1] > counter[-1]:
    print('APPROVED')
else:
    print('REJECTED')