n=int(input())
for _ in range(n):
    word=input()
    a=word[0]
    for i in word[1:]:
        if i==a[-1]:
            pass
        else:
            a+=i
    print(a)