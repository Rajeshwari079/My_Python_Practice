

def primeNum(ll,up):
    for i in range(ll,up+1):
        if isPrime(i):
            print(i,end=" ")

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True

ll=int(input("Enter ll : "))
up=int(input("Enter up : "))

primeNum(ll,up)
