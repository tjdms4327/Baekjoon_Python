import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dumi = []
for _ in range(m):
    k = int(input())
    books = list(map(int, input().split()))
    dumi.append(books)
    
for book in dumi:
    if book != sorted(book, reverse=True):
        print('No')
        sys.exit()
print('Yes')