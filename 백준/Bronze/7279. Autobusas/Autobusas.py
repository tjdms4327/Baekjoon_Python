import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stand = []
people = 0
for _ in range(n):
    a, b = map(int, input().split())
    people += (a-b)
    stand.append(people-k if people > k else 0)
print(max(stand))