import sys
input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    if line == [-1]:
        sys.exit()
        
    cnt = 0
    for x in line[:-1]:
        if 2*x in line[:-1]:
            cnt += 1
            
    print(cnt)