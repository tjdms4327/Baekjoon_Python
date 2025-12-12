import sys
input = sys.stdin.readline

mom = input().strip()
dad = input().strip()

x = int(input())
for _ in range(x):
    baby = input().strip()
    possible = True
    for i in range(5):
        ch = baby[i]
        s_m, s_d = mom[2*i:2*i+2], dad[2*i:2*i+2]
        if ch.isupper():
            if ch in s_m or ch in s_d:
                continue
            else:
                possible = False
                break
        else:
            if ch in s_m and ch in s_d:
                continue
            else:
                possible = False
                break
    
    if possible:
        print('Possible baby.')
    else:
        print('Not their baby!')