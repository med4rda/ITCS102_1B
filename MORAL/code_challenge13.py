name = input("Input your name: ")
print("-------------------------------------")
print("ODD NUMBER SUMMATION, Press 0 to stop")
print("-------------------------------------")

number = 0
sum = 0
odd = ""

while number == 0:
    
    input_num = int(input("Input any number: "))

    if input_num % 2 == 1:
        sum += input_num
        odd += str(input_num) + " "
        print("Odd number detected! The code continues...")
        continue
    
    elif input_num == 0:
        print(f"PROGRAM STOPS.\nHi {name}, the sum of all odd number is {sum}")
        print("Odd numbers detected:",odd)
        break
    else:
        if int(input_num % 2 == 0):
            print("Even number detected! The code continues...")
            continue
        else:
            print("Invalid input")