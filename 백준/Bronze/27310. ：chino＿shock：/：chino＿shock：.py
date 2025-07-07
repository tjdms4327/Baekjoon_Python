emoji=input()

level=len(emoji) + emoji.count(':') + emoji.count('_')*5
print(level)