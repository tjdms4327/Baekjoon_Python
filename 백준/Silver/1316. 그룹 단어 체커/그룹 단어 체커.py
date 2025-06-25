groupnum=0

n=int(input())
for _ in range(n):
    word=input()
    lword=len(word)
    is_group=True
    from string import ascii_lowercase
    alpha_list=list(ascii_lowercase)
    for i in range(lword):
        if word[i] in alpha_list:
            alpha_list.remove(word[i])
        else:  
            if word[i]!=word[i-1]:
                is_group=False
                break
    if is_group:
        groupnum+=1
print(groupnum)