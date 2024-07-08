def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        else:
            return True

def revrse(num):
    rev=0
    dum=num
    while dum!=0:
        rem =dum %10
        rev= rev*10+ rem
        dum//=10
    return rev

def isPaliPrime(n):
    rev=revrse(n)
    if isPrime(n) and n==rev:
        return True
    else:
        return False
    
def PaliPrimeRange(ll,up):
    for i in range(ll,up+1):
        if isPaliPrime(i):
            print(i,end=" ")

ll=int(input("Enter ll : "))
up = int(input("Enter up : "))

PaliPrimeRange(ll,up)