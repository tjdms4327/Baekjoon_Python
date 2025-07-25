s=input()
left, sep, right=s.partition('(^0^)')

print(left.count('@'), right.count('@'))