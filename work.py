def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print("The factorial of", number, "is", result)
