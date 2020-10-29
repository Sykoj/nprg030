

def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

print('Factorial of 5: ' + str(factorial(5)))
print('Factorial of 8: ' + str(factorial(8)))
