# input = [11,22,33,44,55,66]
# output = [22,11,44,33,66,55]

l=eval(input())
i=0
while i<len(l):
    l[i],l[i+1]=l[i+1],l[i]
    i+=2
print(l)