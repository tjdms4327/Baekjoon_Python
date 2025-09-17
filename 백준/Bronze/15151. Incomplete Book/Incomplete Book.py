import sys
input = sys.stdin.readline

k, d = map(int, input().split())

book = 0
tmp = 1
while d > 0:
    d -= tmp * k
    book += 1
    tmp *= 2
if d < 0: book -= 1
print(book)