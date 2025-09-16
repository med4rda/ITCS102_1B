print("The Factorial Program")
number = eval(input("Enter any number: "))
factorial = 1
for i in range(number, 0, -1):
    factorial *= i
print("the facotorial of", number, "is", factorial)