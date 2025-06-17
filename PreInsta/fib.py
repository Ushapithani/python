def fibonacci(n):
    series=[0,1]
    for i in range(2,n-1):
        series.append(series[i-1]+series[i-2])
    return series[:n]
n=int(input("enter a number to get a fibbonacci series range :"))
print("fibonacci series from a given range", fibonacci(n))
