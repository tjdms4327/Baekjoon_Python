n=int(input())
s_list=[1 for _ in range(n) if input().startswith('C')]
print(sum(s_list))