import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    M = list(map(int, input().split()))
    L = list(map(int, input().split()))
    
    mark, leti = sum(M), sum(L)
    mark_round = -1
    leti_round = -1
    for i in range(2, n):
        if mark_round == -1 and M[i] == M[i-1] == M[i-2]:
            mark_round = i
        if leti_round == -1 and L[i] == L[i-1] == L[i-2]:
            leti_round = i
    if mark_round != -1 and leti_round != -1:
        if mark_round < leti_round:
            mark += 30
        elif leti_round < mark_round:
            leti += 30
    elif mark_round != -1:
        mark += 30
    elif leti_round != -1:
        leti += 30    
    
    if mark > leti:
        print("M")
    elif mark < leti:
        print("L")
    else:
        print("T")