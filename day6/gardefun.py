import grade as gf

gradebook = {}
print("\tStudent Gradebook App")

while True:
    print("\nChoices:")
    print("1. Add student")
    print("2. View all students")
    print("3. Find student")

    print("4. Update student marks")
    print("5. Delete student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        gf.add_student(gradebook)
    elif choice == 2:
        gf.view_students(gradebook)
    elif choice == 3:
        gf.find_student(gradebook)
    elif choice == 4:
        gf.update_marks(gradebook)
    elif choice == 5:
        gf.delete_student(gradebook)
    elif choice == 6:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1-6.")