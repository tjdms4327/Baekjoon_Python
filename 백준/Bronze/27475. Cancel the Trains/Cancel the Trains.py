t=int(input())
for _ in range(t):
    n, m=map(int, input().split())
    n_train=list(map(int, input().split()))
    m_train=list(map(int, input().split()))
    cnt=0
    for i in n_train:
        for j in m_train:
            if i==j:
                cnt+=1
                #print('cnt:', cnt, '/ i, j:', i, j , ' / t:', (i*j)**0.5)
    print(cnt)