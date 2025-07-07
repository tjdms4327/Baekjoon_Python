def count_cells(m,n):
    if m==1:
        return n
    elif n==1:
        return m
    return 2*(n+m)-4

m=int(input())
n=int(input())

print(count_cells(m,n))