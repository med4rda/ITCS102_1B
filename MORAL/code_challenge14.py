print("STUDENT INFORMATION SYSTEM")
print("==========================")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING")
    print("A. Add student record")
    print("B. Drift student record")
    print("C. Search student record")
    print("D. Delete student record")
    print("E. Edit student record")
    print("F. Export student record")
    print("G. Exit")

    choice = input("SELECT FROM THE CHOICES ABOVE: ").lower()
    if choice == "a":
        id_no = input("enter your student ID number: ")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = input("enter your age: ")
        course = input("enter your course: ")
        section = input("enter your section: ")
        
        student_record[id_no] = [first_name, last_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")
        print("-----------------------")
        continue

    if choice == "b":
        print(student_record)
        continue     
    if choice == "c":
        id_no = input("enter your student ID number: ")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = input("enter your age: ")
        course = input("enter your course: ")
        section = input("enter your section: ")
        continue
    if choice == "d":
        id_no = input("enter your student ID number: ")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = input("enter your age: ")
        course = input("enter your course: ")
        section = input("enter your section: ")
        continue
    if choice == "e":
        id_no = input("enter your student ID number: ")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = input("enter your age: ")
        course = input("enter your course: ")
        section = input("enter your section: ")
        continue
    if choice == "f":
        id_no = input("enter your student ID number: ")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = input("enter your age: ")
        course = input("enter your course: ")
        section = input("enter your section: ")
        continue
    if choice == "g":
        print("EXITING SYSTEM...")
        break
    else:
        print("INVALID INPUT")
        break


