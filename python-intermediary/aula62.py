#Recursiva fatorial

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n -1)

print(factorial(5))
print(factorial(10))
print(factorial(100))