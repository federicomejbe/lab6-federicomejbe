from grades_manager import *

print("Welcome to the Student Grades Manager!\n")
my_grades = {}
option = input("Select an option:\n1. Add a student\n2. Print student grade averages\n3. Exit\n")
while option != "3":
    if option == "1":
        my_grades = add_student(my_grades)
    elif option == "2":
        sub_option = input("Select an option:\na. Display all students\nb. Display selected students\n")
        if sub_option == "a":
            avg_by_student(my_grades)
        elif sub_option == "b":
            names = input("Enter student names (comma-separated): ")
            keys = names.split(",")
            clean_keys = []
            for name in keys:
                clean_keys.append(name.strip())
            avg_by_student(my_grades, clean_keys)
        else:
            print("Invalid option selected!")
    else:
        print("Invalid option selected!")
    print()
    option = input("Select an option:\n1. Add a student\n2. Print student grade averages\n3. Exit\n")
print("\nGoodbye!")