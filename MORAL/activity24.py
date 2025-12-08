from activity24_1 import GreetPersonName,GreetInfo

# Creating or defining your own function
# Code reusability
# Keyword -- def


def GreetPerson():
    print("\nHi visitor, welcome to my first function")
    print("Please browse around")


GreetPersonName('Paulo')
GreetInfo('Paulo', 'Lucena', '23')


while True:
    print("\nCode Compiler Program")
    print("A - First Program \nB - Second Program \nC - Exit")
    start = input("Select from the options: ").lower()

    if start == "a":
        GreetPersonName("Paulo")
        continue
    elif start == "b":
        GreetInfo("Paulo", "Lucena", "23")
        continue
    elif start == "c":
        print("\nSystem Exit")
        break
    else:
        print("\nInvalid Choice")
        continue