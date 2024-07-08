def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

def pyramid(series, n):
    index = 0
    for i in range(1, n + 1):
        line = []
        for j in range(i):
            if index < len(series):
                line.append(series[index])
                index += 1
        line_str = " ".join(str(num) for num in line)
        print(line_str.center(n * 4))  # Adjust spacing for better formatting

# Number of n in the pyramid
n = 4
# Generate enough Fibonacci numbers for the pyramid
series = fibonacci(n * (n + 1) // 2)
pyramid(series, n)
