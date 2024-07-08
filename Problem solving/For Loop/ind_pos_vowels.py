s=input()
V='aeiouAEIOU'
for i in range(len(s)):
    if s[i].isalpha() and s[i] in V:
        print( f"{s[i]} : {i}")
