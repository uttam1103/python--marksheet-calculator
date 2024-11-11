# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

# Function to check if the student passed
def check_pass_fail(marks):
    fail_count = 0
    grace_applied = False

    # Check each subject for failing marks
    for subject, mark in marks.items():
        if mark < 33:
            if 30 <= mark <= 32 and not grace_applied:
                print(f"Grace marks applied to {subject}. Original Marks: {mark}, Updated Marks: 33")
                marks[subject] = 33 
                grace_applied = True
            else:
                fail_count += 1

    # Determine if the student has passed
    return "Pass" if fail_count == 0 else "Fail"

# Function to display the marksheet
def display_marksheet(student_name, father_name, school_name, board_name, marks ,session):
    total_marks = sum(marks.values())
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)
    result = check_pass_fail(marks)

    # Display the marksheet
    print("\n------ Marksheet ------")
    print(f"Student Name      : {student_name}")
    print(f"Father's Name     : {father_name}")
    print(f"School Name       : {school_name}")
    print(f"Board Name        : {board_name}")
    print(f"session           : {session}")
    print("\nSubject-wise Marks:")
    for subject, mark in marks.items():
        print(f"{subject:18} : {mark}")

    print("\nTotal Marks       : ", total_marks)
    print(f"Percentage        : {percentage:.2f}%")
    print(f"Grade             : {grade}")
    print(f"Result            : {result}")
    print("------------------------")

# Main program
def main():
    # Input student details
    student_name = input("Enter the student's name: ")
    father_name = input("Enter the father's name: ")
    school_name = input("Enter the school name: ")
    board_name = input("Enter the board name: ")
    session = input("Enter the session: ")

    # Input marks for 5 subjects
    marks = {}
    subjects = ["Physics", "Chemistry", "Maths", "English", "Physical Education"]
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter numeric marks.")

    # Display the marksheet
    display_marksheet(student_name, father_name, school_name, board_name, marks,session)

if __name__ == "__main__":
    main()



