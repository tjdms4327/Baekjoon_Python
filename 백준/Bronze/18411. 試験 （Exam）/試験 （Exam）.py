score=list(map(int, input().split()))
score.sort()

print(sum(score[1:]))