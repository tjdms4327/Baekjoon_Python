n = int(input())
for _ in range(n):
    s = input()
    D=s.find('D')
    if D>=0:
        print(D)
    else:
        print(len(s))