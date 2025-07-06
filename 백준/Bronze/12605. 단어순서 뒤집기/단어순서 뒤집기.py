n=int(input())
for i in range(1,n+1):
    s=list(input().split(" "))
    s.reverse()
    print(f"Case #{i}:", *s)