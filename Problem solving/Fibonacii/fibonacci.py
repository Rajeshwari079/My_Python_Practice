def fibonacci(n):
    series = [1, 2]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

def pyramid(series,n):
    space=n-1
    num=1
    k=0
    
    for r in range (1,n+1):
        
        for s in range(1,space+1):
            print(" ",end="")
        for c in range(1,num+1):
            a=series[k]
            print(a,end=" ")
            k+=1

        print()
        space-=1
        num+=1






# Number of n in the pyramid
n = int(input("Enter a no of levels : "))
# Generate enough Fibonacci numbers for the pyramid
series = fibonacci(n * (n + 1) // 2)
pyramid(series, n)