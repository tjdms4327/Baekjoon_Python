n=input().lower()
while n!='#':
    print(n.count('a')+n.count('e')+n.count('i')+n.count('o')+n.count('u'))
    n=input().lower()