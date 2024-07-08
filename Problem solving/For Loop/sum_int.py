s=input()
sum=0
for i in range(len(s)):
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)
