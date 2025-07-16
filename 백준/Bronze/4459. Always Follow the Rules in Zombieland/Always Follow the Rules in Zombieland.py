q=int(input())
quote=[None]
for _ in range(q):
    quote.append(input())

r=int(input())
for _ in range(r):
    a=int(input())
    print(f'Rule {a}: ', end='')
    if a<=0 or a>q:
        print("No such rule")
    else:
        print(quote[a])