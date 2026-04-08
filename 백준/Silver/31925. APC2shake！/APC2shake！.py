import sys
input = sys.stdin.readline

n = int(input())

cand = []
for _ in range(n):
    name, inschool, icpc, shake, apc = input().strip().split()
    shake = int(shake)
    apc = int(apc)
    
    if inschool=='jaehak' and icpc=='notyet' \
        and (shake==-1 or shake>3):
            cand.append((name, apc))
            

cand.sort(key=lambda x: x[1])
cand = cand[:10]

cand.sort(key=lambda x:x[0])
print(len(cand))
for n, _ in cand:
    print(n)
    