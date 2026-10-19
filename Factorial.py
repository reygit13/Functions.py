def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

num = int(input("Give me a number now and gain a factorial, Lasts only till 8 pm 19 oct 2026 BST hurry"))

if num < 0:
    print("ERROR 101 - FACTORIAL NONEXISTENT PLS RETRY IN 999999999 years")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))
