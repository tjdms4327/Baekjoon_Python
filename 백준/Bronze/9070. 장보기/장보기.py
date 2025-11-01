# bronzeII_9070
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    W, C = [], []
    for _ in range(n):
        w, c = map(int, input().split())
        W.append(w)
        C.append(c)
    
    gram_per_won = [W[i]/C[i] for i in range(n)]
    best_choice = max(gram_per_won)
    best_lst = [C[idx] for idx, choice in enumerate(gram_per_won) if choice == best_choice]
    if len(best_lst) == 1:
        print(*best_lst)
    else:
        print(min(best_lst))