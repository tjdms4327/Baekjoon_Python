cand={'Tiger':0, 'Lion':0}
for _ in range(9):
    s=input()
    cand[s]+=1

king=max(cand, key=cand.get)
print(king)