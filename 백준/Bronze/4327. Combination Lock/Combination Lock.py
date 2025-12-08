import sys
input = sys.stdin.readline

while True:
    start, n1, n2, n3 = map(int, input().split())
    if start==n1==n2==n3==0:
        break
    
    tot = 2*40 
    tot += (start - n1) % 40  
    tot += 40 + (n2-n1)%40
    tot += (n2-n3)%40
    print(tot * 9)