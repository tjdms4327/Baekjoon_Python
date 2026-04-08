import sys
input = sys.stdin.readline

n = int(input())

mapping = {'P':0, 'C':1, 'V':2,
           'S':3, 'G':4, 'F':5}

trash = [input().strip() for _ in range(n)]
p = list(map(int, input().split())) # P, C, V, S, G, F
p_O = int(input())

tot = 0
for x in trash:
    if len(set(x))==1 and x[0]!='O':
        c = len(x) * min(p[mapping[x[0]]], p_O)    
    else:
        c = len(x) * p_O
    tot += c
    
print(tot)