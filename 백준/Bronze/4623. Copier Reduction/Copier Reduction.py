import sys
input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())
    if a==b==c==d==0: 
        break
    
    a, b = min(a,b), max(a,b)
    c, d = min(c,d), max(c,d)
    if a<=c and b<=d:
        print('100%')
    else:
        x_per = (c*100)//a
        y_per = (d*100)//b
        print(f'{min(x_per, y_per)}%')