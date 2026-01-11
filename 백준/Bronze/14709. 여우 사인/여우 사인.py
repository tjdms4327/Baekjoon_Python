import sys
input = sys.stdin.readline

n = int(input())

fingers = set()
for _ in range(n):
    a, b = map(int, input().split())
    fingers.add((min(a, b), max(a, b)))

if fingers == {(1, 3), (3, 4), (1, 4)}:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')