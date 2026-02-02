import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

cards = list(range(1, 2*n+1))
for _ in range(m):
    k = int(input())
    
    if k == 0:
        A = cards[:n]
        B = cards[n:]
        new_cards = []
        for i in range(n):
            new_cards.append(A[i])
            new_cards.append(B[i])
        cards = new_cards
    else:
        cards = cards[k:] + cards[:k]
        
print(*cards, sep='\n')