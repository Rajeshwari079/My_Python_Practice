s=input()
b=input()
c=0
for i in range(len(s)):
    if s[i:i+len(b):]==b:
        c+=1
print(c)