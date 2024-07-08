s=input()
rev=''
for i in s:
    rev=i+rev
print("using for : ",rev)

revv=''
j=len(s)-1
while i>=0:
    rev=rev+s[i]
    i-=1
print("using while : ",revv)

