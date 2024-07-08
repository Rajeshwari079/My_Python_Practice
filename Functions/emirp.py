# num should be prime
# num rev also should be prime
# num sholud not be palindrome

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
        
def reverse(n):
    rev=0
    dum=n
    while n>0:
        rem=dum%10
        dum//=10
        rev=rev*10 + rem
    return rev


    
def emirp(n):
    re= reverse(n)
    if isPrime(n) and isPrime(re) and re!=n:
        return True
    else:
        return False
    
def emirpRange(ll,up):
    for i in range(ll,up+1):
        if emirp(i):
            print(i,end=" ")
 
ll=int(input("Enter ll : "))
up = int(input("Enter up : "))

emirpRange(ll,up)