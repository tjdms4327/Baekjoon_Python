def reverse_card(list_card, a, b):
    a-=1
    b-=1
    #print(list[a:b+1])
    for i in range((b-a+1)//2):
        list_card[a + i], list_card[b - i] = list_card[b - i], list_card[a + i]
    #print(list[a:b+1])
    #print(list)
    return list_card

list_card=[i for i in range(1,21)]
for _ in range(10):
    a,b=map(int, input().split())
    list_card = reverse_card(list_card, a, b)
print(*list_card, sep=' ')
    