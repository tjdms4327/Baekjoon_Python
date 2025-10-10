# bronzeIII_33631
import sys
input = sys.stdin.readline

def query(n, i):
    global having, cookie
    if n == 1:
        for x in range(4):
            if ingredient[x]*i > having[x]:
                return 'Hello, siumii'
        for x in range(4):
            having[x] -= ingredient[x]*i
        cookie += i
        return cookie
    else:
        having[n-2] += i
        return having[n-2]

having = list(map(int, input().split()))
ingredient = list(map(int, input().split()))

cookie = 0
q = int(input())
for _ in range(q):
    n, i = map(int, input().split())
    print(query(n, i))