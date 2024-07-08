s=input()
sum=0
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])%2==0 and i%2!=0:
            sum+=int(s[i])
print(sum)