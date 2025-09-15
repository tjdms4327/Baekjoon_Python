import sys
input = sys.stdin.readline

while True: 
    h1, m1, h2, m2 = map(int, input().split())
    if h1==m1==h2==m2==0: break
    
    if (h2 < h1) or (h2 == h1 and m2 < m1):
        h1 -= 24
    m2 -= m1
    m2 += (h2 - h1) * 60
    print(m2)