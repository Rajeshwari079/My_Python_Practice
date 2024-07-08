n=int(input())
a=int(input())
b=int(input())
print('------------------------------------')
if n==1:
    print(a)

elif n==2:
    print(a)
    print(b)

else:
    print(a)
    print(b)
    for i in range(n-2):
        next=a+b
        print(next)
        a,b=b,next
    
