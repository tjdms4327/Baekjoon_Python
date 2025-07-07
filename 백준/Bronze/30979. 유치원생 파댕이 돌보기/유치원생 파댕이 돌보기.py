T=int(input())
N=int(input())
F_list=list(map(int, input().split()))

candy_sum=sum(F_list)
if candy_sum>=T:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')