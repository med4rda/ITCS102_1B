name = input("What is your name? ")
fare = eval(input("Fare fee: "))
isStudent = input("Are you currently a student (yes/no) : ")

if isStudent.lower() == "yes":
    discount = fare * 0.2
    new_fare = fare - discount
    print("Hi,", name)
    print("Your discount is : ",discount)
    print("Your new fare is : ",new_fare)
else:
    print(f"Sorry, {name}, you are not eligible for a student discount.")