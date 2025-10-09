temp = input("Input Temperature: ")
if int(temp.isnumeric()):
    if int(temp) <= 0:
        print("Your temperature is below freezing")
    elif int(temp) >=1 and int(temp) <= 15:
        print("Your temperature is extreme cold")
    elif int(temp) >= 16 and int(temp) <= 30:
        print("Your temperature is cold")
    elif int(temp) >= 31 and int(temp) <= 38:
        print("Your Temperature is lukewarm")
    elif int(temp) >= 39 and int(temp) <= 42:
        print("Your temperature is warm")
    elif int(temp) >= 43 and int(temp) <= 50:
        print("Your temperature is hot temp")
    elif int(temp) >= 51 and int(temp) <= 60:
        print("Your temperature is extremely hot temp")
    elif int(temp) >= 61:
        print("Your temperature is burning temp")
else:
    print("Invalid temp")