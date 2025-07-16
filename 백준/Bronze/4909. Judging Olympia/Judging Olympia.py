while True:
    scores=list(map(float, input().split()))
    if set(scores)=={0.0}: break

    scores.sort()
    result=sum(scores[1:-1])/4
    print(f'{result:g}') # 불필요한 .0 제거