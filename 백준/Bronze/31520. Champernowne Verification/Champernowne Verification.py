def Champernowne(n):
    i=1
    while len(n) >= len(str(i)):
        str_i=str(i)
        if n.startswith(str_i):
            len_i=len(str_i)
            n=n[len_i:]
            i+=1
        else:
            return -1
    return i-1

n=input()
print(Champernowne(n))