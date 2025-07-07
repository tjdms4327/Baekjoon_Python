def no_duplicate(s):
    result=s[0]

    for char in s[1:]:
        if char!=result[-1]:
            result+=char

    return result

s=input()
print(no_duplicate(s))
