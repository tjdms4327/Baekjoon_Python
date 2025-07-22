t=int(input())
for _ in range(t):
    n=int(input())

    clothes={}
    for i in range(n):
        b, a=input().split()
        if a in clothes:
            clothes[a].append(b)
        else:
            clothes[a]=[b]
            
    # 조합
    res = 1
    for kinds in clothes.values():
        res *= (len(kinds) + 1)  # 각 종류에서 입지 않는 경우 포함
    print(res - 1)  # 모두 안 입는 경우 제외