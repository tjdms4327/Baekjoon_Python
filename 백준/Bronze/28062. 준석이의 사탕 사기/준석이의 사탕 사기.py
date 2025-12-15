import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

odd = [x for x in sorted(A) if x%2==1]

tot = sum(A)
while tot%2 != 0:
    tot -= odd.pop(0)
print(tot)