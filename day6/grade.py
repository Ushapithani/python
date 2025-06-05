def add_student(gradebook):
    name = input("Enter Student Name: ")
    num_subjects = int(input("Enter number of subjects: "))
    subjects = {}
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks
    gradebook[name] = subjects

def view_students(gradebook):
    for i in gradebook:
        length = len(gradebook[i])
        sum = 0
        for marks in gradebook[i]:
            sum += gradebook[i][marks]
        avg = sum / length

        print(f"{i} => avg : {avg} \n{gradebook[i]}")
def find_student(name,subject):
    



def update_marks(gradebook):
    name = input("Enter student name to update: ")
    if name in gradebook:
        subject = input("Enter subject to update: ")
        if subject in gradebook[name]:
            new_mark = float(input(f"Enter new marks for {subject}: "))
            gradebook[name][subject] = new_mark
            print("Marks updated!")
        else:
            print("Subject not found!")
    else:
        print("Student not found!")

def delete_student(gradebook):
    name = input("Enter student name to delete: ")
    if name in gradebook:
        del gradebook[name]
        print("Student removed from gradebook.")
    else:
        print("Student not found!")