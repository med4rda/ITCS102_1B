import sys

def pause():
    input("\nPress ENTER to return to the menu...")

# ======================================================
# Topic Programs
# ======================================================

# --- PRINT STATEMENTS ---
def define_print():
    print("\nPRINT STATEMENT\n")
    print("The print statement is used to display information on the screen.")
    print('We use the "print()" function')
    pause()
def print_examples():
    print("\nPRINT STATEMENT EXAMPLES\n")
    print("Example 1: print('Hello World!')")
    print("\nOutput:")
    print("Hello World!\n")

    print('Example 2: print("Sum:", 5 + 3)')
    print("\nOutput:")
    print("Sum: 8")
    pause()

# --- VARIABLES ---
def define_variables():
    print("\nVARIABLES\n")
    print("A variable is a name that stores a value in a program.\nIt acts like a container or box that holds data.\nYou can create a variable by giving it a name and a value.")
    pause()
def variables_example():
    print("\nVARIABLES EXAMPLE\n")
    print('name = "Paulopogi"')
    print("print(name)")
    print("\nOutput:\nPaulopogi")
    pause()

# --- OPERATORS ---
def define_operators():
    print("\nOPERATORS\n")
    print("Operators are symbols used to perform actions in Python.")
    pause()
def operators_example():
    print("\nOPERATORS EXAMPLE\n")
    print("Arithmetic: 7 + 3 =", 7 + 3)
    print("Comparison: 7 > 3 =", (7 > 3))
    print("Logical: True and False =", (True and False))
    pause()

# --- CONDITIONALS ---
def define_conditionals():
    print("\nCONDITIONALS\n")
    print("Conditionals are used to make decisions in a program.\nThey check if something is true or false, \nand then the computer chooses what action to do.\n\nWe use the keywords:")
    print("if, elif, else")
    pause()
def conditionals_example():
    print("\nCONDITIONALS EXAMPLE\n")
    print('score = 85\n\nif score >= 90:\n    print("Grade: A")\nelif score >= 80:\n    print("Grade: B")\nelif score >= 70:\n    print("Grade: C")\nelse:\n    print("Grade: D")')
    print("\nOutput:\nGrade: B")
    pause()

# --- LOOPS ---
def define_loops():
    print("\nLOOPS\n")
    print("A for loop is used to repeat a block of code for each item \nin a sequence such as a list, string, or range of numbers. \nIt allows you to run the same instructions many times automatically.")
    pause()
def loops_example():
    print("\nLOOPS EXAMPLE\n")
    print('fruits = ["apple", "banana", "mango"]\n\nfor fruit in fruits:\n    print(fruit)')
    print("\nOutput:\napple\nbanana\nmango")

    pause()

# --- LISTS ---

def define_lists():
    print("\nLISTS\n")
    print("A list in Python is a collection of items stored in a single variable.\nA list can hold multiple values at the same time, \nsuch as numbers, strings, or even other lists.")
    print("Created using square brackets: [ ]")
    pause()
def lists_example():
    print("\nLISTS EXAMPLE\n")
    print('fruits = ["apple", "banana", "mango"]\nprint(fruits)')
    print('\nOutput:\n["apple", "banana", "mango"]')
    pause()

# --- FUNCTIONS ---
def define_functions():
    print("\nFUNCTIONS\n")
    print("A function in Python is a block of organized,\nreusable code that performs a specific task. \nYou create it once, and you can call it many times.")
    print('Defined using the keyword "def"')
    pause()

def functions_example():
    print("\nFUNCTIONS EXAMPLE\n")

    print('def greet():\n    print("Hello, Welcome!")')
    print("\nCalling the function:\ngreet()")
    print("\nOutput:\nHello, Welcome!")
    pause()

# ======================================================
# SUBMENUS
# ======================================================

def submenu_print():
    while True:
        print("\nPRINT STATEMENTS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_print()
        elif choice == "2":
            print_examples()
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

def submenu_variables():
    while True:
        print("\nVARIABLES MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_variables()
        elif choice == "2":
            variables_example()
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

def submenu_operators():
    while True:
        print("\nOPERATORS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_operators()
        elif choice == "2":
            operators_example() 
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

def submenu_conditionals():
    while True:
        print("\nCONDITIONALS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_conditionals()
        elif choice == "2":
            conditionals_example()    
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

def submenu_loops():
    while True:
        print("\nLOOPS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_loops()
        elif choice == "2":
            loops_example()
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

def submenu_lists():
    while True:
        print("\nLISTS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_lists()
        elif choice == "2":
            lists_example()
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")


def submenu_functions():
    while True:
        print("\nFUNCTIONS MENU\n")
        print("1. Definition")
        print("2. Example")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ")

        if choice == "1":
            define_functions()
        elif choice == "2":
            functions_example()
        elif choice == "3":
            return
        else:
            print("\nInvalid input, try again.\n")

# ======================================================
# USER-DEFINED PROGRAM RUNNER
# ======================================================

def run_user_code():
    print("\nRUN YOUR OWN PYTHON CODE\n")
    print("Type your code below. Type 'DONE' on a new line to execute.\n")

    code = ""

    while True:
        line = input(">>> ")
        if line.lower() == "done":
            break
        code += line + "\n"

    try:
        exec(code)
        print("\n✅ Program ran successfully!")
    except Exception as error:
        print("\n❌ Error:", error)

    pause()

# ======================================================
# MAIN MENU
# ======================================================

def main_menu():
    while True:
        print("\nSELECT THE TOPIC YOU WANT TO LEARN\n")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("8. Run Your Own Python Program")
        print("9. Exit")

        choice = input("\nEnter: ")

        if choice == "1":
            submenu_print()
        elif choice == "2":
            submenu_variables()
        elif choice == "3":
            submenu_operators()
        elif choice == "4":
            submenu_conditionals()
        elif choice == "5":
            submenu_loops()
        elif choice == "6":
            submenu_lists()
        elif choice == "7":
            submenu_functions()
        elif choice == "8":
            run_user_code()
        elif choice == "9":
            print("\nThank you for using the program. Goodbye!\n")
            sys.exit()
        else:
            print("\nInvalid choice. Try again.\n")

# Start the program
print("\nWELCOME TO PYTHON LEARNING SYSTEM!\n")

name = input("Enter your name: ")
start = input(f"\nHi {name}! Do you want to start learning python today?\n\n1. Yes \n2. No \n\nEnter: ")
if start == "1":
    main_menu()
elif start == "2":
    print("\nThank you for using the program. Goodbye!\n")
    sys.exit()
else:
    print("\nInvalid entry. Please try again.\n")
    sys.exit()