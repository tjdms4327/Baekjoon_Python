s=input()

length=len(s)
words=[]
for i in range(1, length-1):
  for j in range(i+1, length):
    A, B, C = s[:i], s[i:j], s[j:]
    new_word = A[::-1]+B[::-1]+C[::-1]
    words.append(new_word)
words.sort()
print(words[0])