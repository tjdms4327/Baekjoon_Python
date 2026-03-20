import sys
input = sys.stdin.readline

def nautilus_sequence(lst):
    for i in range(len(lst)):
        if i < 4:
            if lst[i]!=i:
                return False
        else:
            if lst[i] != sum(lst[i-4:i]):
                return False
    return True

n = int(input())
for _ in range(n):
    M = list(map(int, input().split()))
    
    nautilus = nautilus_sequence(M)
    if nautilus:
        print('NAUTILUS')
    else:
        print('SNAIL')