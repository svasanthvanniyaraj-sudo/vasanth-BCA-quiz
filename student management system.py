students=[]
while True:
    print("\n***Student Management System***")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice=input("Enter your choice")
    if choice=="1":
        name=input("Enter student name:")
        students.append(name)
        print("Student add successfully!")
    elif choice=="2":
        print("Student list:")
        for student in students:
            print(student)
    elif choice=="3":
        print("Search Student")
        name=input("Enter the student name:")
        if name in students:
            print("Student found!")
        else:
            print("Student not found!")
    elif choice=="4":
        print("Delete student")
        name=input("Enter the  student name to delete:")
        if name in students:
            students.remove(name)
            print("Student deleted")
        else:
            print("Student not found")
    elif choice=="5":
        print("Thank you!")
        break
    else:
        print("In-valid choice!")
        
