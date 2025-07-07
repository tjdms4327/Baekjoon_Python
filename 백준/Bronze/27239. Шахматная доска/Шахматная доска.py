def find_pos(n):
    row=(n-1)%8 + 97
    col=(n-1)//8
    return chr(row)+str(col+1)    

n=int(input())

print(find_pos(n))