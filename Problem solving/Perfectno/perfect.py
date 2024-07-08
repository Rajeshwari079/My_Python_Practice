n=int(input())

sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i

print(sum)
if sum==n:
    print("Perfect no")
else:
    print("Not a perfect no.")