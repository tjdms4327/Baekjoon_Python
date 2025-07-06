b,c,d=map(int, input().split())
buger=list(map(int, input().split()))
side=list(map(int, input().split()))
drink=list(map(int, input().split()))

print(sum(buger)+sum(side)+sum(drink))

set_menu=min(b,c,d)
buger.sort(reverse=True); side.sort(reverse=True); drink.sort(reverse=True)
set_price=0
for i in range(set_menu):
    set_price+=(buger[i]+side[i]+drink[i])*0.9
print(int(set_price+sum(buger[set_menu:])+sum(side[set_menu:])+sum(drink[set_menu:])))