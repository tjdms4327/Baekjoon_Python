# bronzeIII_13684
import sys
input = sys.stdin.readline

while True:  
    k = int(input())
    if k == 0: break
    
    n, m = map(int, input().split())
    for _ in range(k):
        x, y = map(int, input().split())
        if x == n or y == m:
            print('divisa')
        elif x > n:
            if y > m:
                print('NE')
            else:
                print('SE')
        elif x < n:
            if y > m:
                print('NO')
            else:
                print('SO')