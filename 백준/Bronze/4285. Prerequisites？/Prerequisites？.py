import sys
input = sys.stdin.readline

while True:
    line = input().split()
    if line[0] == '0': 
        break

    k, m = map(int, line)
    selected = set(input().split())

    ok = True
    for _ in range(m):
        data = input().split()
        c, r = map(int, data[:2])
        courses = data[2:]
        
        cnt = sum(1 for x in courses if x in selected)
        
        if cnt < r:
            ok = False
    print("yes" if ok else "no")