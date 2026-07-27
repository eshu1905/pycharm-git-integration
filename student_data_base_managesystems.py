class StudentDatabaseManagementSystem:

    def __init__(self):
        self.file_name = "students.txt"

    # Add Student
    def add_student(self):
        file = open(self.file_name, "a")

        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        file.write(f"{roll_no},{name},{age},{course}\n")
        file.close()

        print("Student Added Successfully.\n")

    # View Students
    def view_students(self):
        file = open(self.file_name, "r")

        data = file.read()

        if data:
            print("\n------ Student Records ------")
            print("Roll No\tName\tAge\tCourse")
            print("-" * 40)

            records = data.split("\n")

            for record in records:
                if record != "":
                    student = record.split(",")
                    print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}")
        else:
            print("No Student Records Found.")

        file.close()

    # Search Student
    def search_student(self):
        roll = input("Enter Roll Number to Search: ")

        file = open(self.file_name, "r")
        found = False

        for line in file:
            student = line.strip().split(",")

            if student[0] == roll:
                print("\nStudent Found")
                print("Roll No :", student[0])
                print("Name    :", student[1])
                print("Age     :", student[2])
                print("Course  :", student[3])
                found = True
                break

        if not found:
            print("Student Not Found.")

        file.close()

    # Update Student
    def update_student(self):
        roll = input("Enter Roll Number to Update: ")

        file = open(self.file_name, "r")
        students = file.readlines()
        file.close()

        file = open(self.file_name, "w")

        found = False

        for line in students:
            student = line.strip().split(",")

            if student[0] == roll:
                print("Enter New Details")

                name = input("Enter Name: ")
                age = input("Enter Age: ")
                course = input("Enter Course: ")

                file.write(f"{roll},{name},{age},{course}\n")
                found = True
            else:
                file.write(line)

        file.close()

        if found:
            print("Student Updated Successfully.")
        else:
            print("Student Not Found.")

    # Delete Student
    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")

        file = open(self.file_name, "r")
        students = file.readlines()
        file.close()

        file = open(self.file_name, "w")

        found = False

        for line in students:
            student = line.strip().split(",")

            if student[0] != roll:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Student Deleted Successfully.")
        else:
            print("Student Not Found.")

    # Menu
    def menu(self):

        while True:

            print("\n========== Student Database Management System ==========")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice.")


obj = StudentDatabaseManagementSystem()
obj.menu()