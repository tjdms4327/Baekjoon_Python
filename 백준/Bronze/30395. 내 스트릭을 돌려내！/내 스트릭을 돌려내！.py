import sys
input = sys.stdin.readline

n = int(input())
record = list(map(int, input().split()))

max_strick = 0
strick = 0
freeze_c = 0
freeze = True
for x in record:
    if x > 0:
        strick += 1
    else:
        if freeze:
            freeze = False
        else:
            max_strick = max(max_strick, strick)
            strick = 0
    
    if not freeze and freeze_c<2:
        freeze_c += 1
    if freeze_c == 2:
        freeze = True
        freeze_c = 0
        
max_strick = max(max_strick, strick)
print(max_strick)