t=int(input())
for _ in range(t):
    idx, s=input().split()
    idx=int(idx)-1

    new_s=''.join([c for i, c in enumerate(s) if i!=idx])
    print(new_s)
    