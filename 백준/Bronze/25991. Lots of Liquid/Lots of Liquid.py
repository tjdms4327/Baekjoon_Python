n=int(input())
lens=list(map(float, input().split()))

liquid=0
for len in lens:
    liquid+=len**3
print(f'{liquid**(1.0/3):.6f}')