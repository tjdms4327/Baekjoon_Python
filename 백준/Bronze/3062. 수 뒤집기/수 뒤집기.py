def sum_num_and_reverse(num):
    num_reverse=num[::-1]
    tot=str(int(num)+int(num_reverse))
    return tot

def symmetry():
    tot=sum_num_and_reverse(num)
    result='YES'
    for i in range(len(tot)//2):
        if tot[i]!=tot[len(tot)-i-1]: result='NO'; break
    return result
    
t=int(input())
for _ in range(t):
    num=input()
    print(symmetry())