def change_wood(wood_list):
    for i in range(4):
        if wood_list[i]>wood_list[i+1]:
            wood_list[i], wood_list[i+1] = wood_list[i+1], wood_list[i]
            print(*wood_list, sep=' ')
    if wood_list!=sorted(wood_list):
        change_wood(wood_list)

wood_list=list(map(int, input().split()))
change_wood(wood_list)