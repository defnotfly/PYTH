def factorial (n):
    if n <= 1:
        return  n
    else:
        return n * factorial(n - 1)

x = int(input("Enter a number: "))
print(factorial(x))