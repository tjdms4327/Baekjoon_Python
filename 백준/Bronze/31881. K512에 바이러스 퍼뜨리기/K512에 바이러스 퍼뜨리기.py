import sys
input = sys.stdin.readline

n, q = map(int, input().split())

virus = [False]*(n+1) #1-indexed
count = 0
for _ in range(q):
    line = input().strip().split()

    if line[0] == '1':
        x = int(line[-1])
        if virus[x] == False:
            count += 1
        virus[x] = True
    elif line[0] == '2':
        x = int(line[-1])
        if virus[x] == True:
            count -= 1
        virus[x] = False
    else:
        print(n - count)
        