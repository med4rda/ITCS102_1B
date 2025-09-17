print("Welcome to the Cartoon Picker!")
print("Just answer the following questions...")
cartoon = str(input("What genre of cartoon do you want to watch?\nChoose only the letter of your answer.\na. Action\nb. Comedy\nc. Fantasy \nAnswer: ")) .lower()
# chose action
if cartoon == "a":
    print("You prefer Action")
    duration = str(input("How long the duration would you like it to be? \na. Short \nb. Medium \nc. Long \nAnswer: ")) .lower()
    if duration == "a":
        print("You prefer: short-duration action cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("Paperman would be the best for you!")
        elif year == "b":
            print("Feast would be the best for you!")
        elif year == "c":
            print("Piper would be the best for you!")
    elif duration == "b":
        print("You prefer: medium-duration action cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("The Simpsons would be the best for you!")
        elif year == "b":
                print("Family Guy would be the best for you!")
        elif year == "c":
                print("Rick and Morty would be the best for you!")
    if duration == "c":
        print(f"You prefer: long-duration action cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("Spongebob would be the best for you!")
        elif year == "b":
            print("South Park would be the best for you!")
        elif year == "c":
            print("Looney Tunes would be the best for you!")
if cartoon == "b":
    print("You prefer Comedy")
    duration = str(input("How long the duration would you like it to be? \na. Short \nb. Medium \nc. Long \nAnswer: ")) .lower()
    if duration == "a":
        print("You prefer: short-duration comedy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("1 would be the best for you!")
        elif year == "b":
            print("2 would be the best for you!")
        elif year == "c":
            print("3 would be the best for you!")
    elif duration == "b":
        print("You prefer: medium-duration comedy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("11 Simpsons would be the best for you!")
        elif year == "b":
            print("22 would be the best for you!")
        elif year == "c":
            print("33 would be the best for you!")
    if duration == "c":
        print(f"You prefer: long-duration comedy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("111 would be the best for you!")
        elif year == "b":
            print("222 would be the best for you!")
        elif year == "c":
            print("333 would be the best for you!")
if cartoon == "c":
    print("You prefer Fantasy")
    duration = str(input("How long the duration would you like it to be? \na. Short \nb. Medium \nc. Long \nAnswer: ")) .lower()
    if duration == "a":
        print("You prefer: short-duration fantasy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("a would be the best for you!")
        elif year == "b":
            print("b would be the best for you!")
        elif year == "c":
            print("c would be the best for you!")
    elif duration == "b":
        print("You prefer: medium-duration fantasy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("aa would be the best for you!")
        elif year == "b":
            print("bb would be the best for you!")
        elif year == "c":
            print("cc would be the best for you!")
    if duration == "c":
        print(f"You prefer: long-duration fantasy cartoon")
        year = input("Which year would you like to start? \na. 2000 \nb. 2010. \nc. 2020 \nAnswer: ") .lower()
        if year == "a":
            print("aaa would be the best for you!")
        elif year == "b":
            print("bbb would be the best for you!")
        elif year == "c":
            print("ccc would be the best for you!")
