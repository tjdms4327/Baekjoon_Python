import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    people = 0
    first = [0]
    for i in range(m):
        p1, p2 = map(int, input().split())
        people += (p1 - p2)
        if people < 0:
            first.append(people)
    print((-1) * min(first))