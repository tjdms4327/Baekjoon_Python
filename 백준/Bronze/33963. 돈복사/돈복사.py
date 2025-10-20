n = input().strip()
len_n = len(n)
n = int(n)

button = 0
while len_n == len(str(n)):
    n *= 2
    button += 1
print(button - 1)