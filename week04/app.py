import mymath

number = int(input("Enter a number: "))
print(f"{number}! = {mymath.factorial_iter(number)}")
print(f"{number}! = {mymath.factorial_recursive(number)}")