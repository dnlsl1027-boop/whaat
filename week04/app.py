import mymath

number = int(input("Enter a number: "))
print(f"{number}! = {mymath.factorial(number)}")
print(f"{number}! = {mymath.factorial_recursive(number)}")