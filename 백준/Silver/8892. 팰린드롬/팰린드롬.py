import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    S = [input().strip() for _ in range(k)]
    
    ok = False
    for i in range(k):
        for j in range(i+1, k):
            slice1 = S[i] + S[j]
            if slice1 == slice1[::-1]:
                ok = True
                print(slice1)
                break
            slice2 = S[j] + S[i]
            if slice2 == slice2[::-1]:
                ok = True
                print(slice2)
                break
        if ok:
            break

    if not ok:
        print(0)
    
    