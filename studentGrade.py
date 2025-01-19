def menu():
    print("========Student Grades Manager========")
    print("[1] Add a new student")
    print("[2] Calculate average grade for a student")
    print("[3] Display all students and thier grades")
    print("[4] Save data to file")
    print("[5] Load data from file")
    print("[6] Exit\n")

def StudentData():
    students = {}  # Dictionary to store student names and their grades
    StudentName = (input("Please enter the Student Name: "))
    StudentGrade = input("Please enter Student Number Grade (comma seperated): ")
    try:
        students[StudentName] = [int(StudentGrade.strip()) for StudentGrade in StudentGrade.split(",")]
        return students
    except ValueError:
        print("Invalid input. Please enter numeric grades separated by commas.")
        return {}

def calculateAverage(StudentGrade):
    if StudentGrade:
        average = sum(StudentGrade) / len(StudentGrade)
        print(f"The average grade is {average:.2f}.")
        return average
    print("No grades to calculate.")
    return 0

def LetterGradePlacement(StudentGrade):
    # Determine the letter grade based on the numeric grade
    if 90 <= StudentGrade <= 100:
        return 'A'
    elif 80 <= StudentGrade < 90:
        return 'B'
    elif 70 <= StudentGrade < 80:
        return 'C'
    elif 60 <= StudentGrade < 70:
        return 'D'
    elif 0 <= StudentGrade < 60:
        return 'F'
    else:
        return 'Invalid Grade'  # Handles cases where the grade is out of range


def DisplayGrades(data):
    return data

def SavetoFile(data):
    pass

def LoadData():
    pass

Student_Data = {}

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        new_data = StudentData()
        if new_data:
            Student_Data.update(new_data)  # Add new students to the dictionary
            print("Student data added.")
        else:
            print("No data was added.")

    elif choice == "2":
        Student_Name = input("Please enter the student name: ")
        if Student_Name in Student_Data:  # Ensure Student_Data is defined
            calculateAverage(Student_Data[Student_Name])
        else:
            print("Student not found. Please add the student first.")

    elif choice == "3":
        DisplayGrades()

    elif choice == "4":
        pass  # Implement SavetoFile(StudentGrades) when needed

    elif choice == "5":
        LoadData()

    elif choice == "6":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid input, please try again.")







# === Student Grades Manager ===
# 1. Add a new student  
# 2. Calculate average grade for a student
# 3. Display all students and their grades
# 4. Save data to file
# 5. Load data from file
# 6. Exit

# Choose an option: 1
# Enter student name: Alice
# Enter grades (comma-separated): 85, 90, 78
# Student Alice added successfully!

# Choose an option: 3
# Alice: [85, 90, 78]

# Choose an option: 2
# Enter student name: Alice
# Average grade for Alice: 84.33

# Choose an option: 4
# Data saved to grades.txt!

# Choose an option: 5
# Data loaded from grades.txt!

# Choose an option: 6
# Goodbye!
