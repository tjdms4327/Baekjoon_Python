s=input()
if ('social' in s) or ('history' in s) or ('language' in s) or ('literacy' in s):
    print('digital humanities')
else: # 무조건 두 집단 중 하나에 속함
    print('public bigdata')