def square(num):
    x=1
    while x<N:
        x*=2
    if x==N:
        return 1
    else:
        return 0


N=int(input())

yesno=square(N)
print(yesno)