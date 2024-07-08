sum=0
n=int(input())
i=1
while i<=n//2:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("Perfeect number")