def find_correct(nums_list, sum_wrongs):
    for i in nums_list:
        if (sum_wrongs-i in nums_list) and (sum_wrongs!=2*i):
            nums_list.remove(i)
            nums_list.remove(sum_wrongs-i)
            break
    print(*nums_list, sep='\n')

nums=[int(input()) for _ in range(9)]
sum_wrongs = sum(nums)-100
find_correct(nums, sum_wrongs)