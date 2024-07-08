l=eval(input())
m=[]
for i in range(len(l)):

    if l[i]%2==0:
         m.append('even')
    else:
        m.append('odd')
print(m)