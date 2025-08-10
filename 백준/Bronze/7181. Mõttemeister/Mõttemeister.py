import sys
input=sys.stdin.readline

def correct(secret, cand):
    correct_num=0
    for i in cand:
        if i in secret:
            correct_num+=1
    
    correct_pos=0
    for i in range(4):
        if secret[i]==cand[i]:
            correct_pos+=1

    return correct_num, correct_pos
    
secret=list(input().strip())
n=int(input())
for _ in range(n):
    cand=list(input().strip())
    print(*correct(secret, cand))
    