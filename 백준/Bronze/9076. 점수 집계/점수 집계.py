t=int(input())
for _ in range(t):
    scores=list(map(int, input().split()))
    scores.sort()
    score=scores[1:-1]
    if score[-1]-score[0]>=4:
        print('KIN')
    else:
        print(sum(score))