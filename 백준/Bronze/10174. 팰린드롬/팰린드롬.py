n=int(input())
for _ in range(n):
    s=input().strip().lower()
    len_s=len(s)

    pal='Yes'
    for i in range(len_s//2):
        if s[i]!=s[len_s-i-1]:
            pal='No'
            break
    print(pal)