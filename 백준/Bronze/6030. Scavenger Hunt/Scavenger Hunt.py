def find_divisors(n):
    divisors=[]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return sorted(divisors)

p,q=map(int, input().split())

Ps=find_divisors(p)
Qs=find_divisors(q)
for i in Ps:
    for j in Qs:
        print(i, j)