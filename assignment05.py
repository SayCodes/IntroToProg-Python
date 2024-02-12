# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sayali Bhosale,2/11/2024, Assignment05:Advanced Collections and Error Handling
# ------------------------------------------------------------------------------------------ #
import sys

# Constants
MENU: str = """

---- Course Registration Program ----
 Select from the following menu: 
  1. Register a Student for a Course
  2. Show current data
  3. Save data to a file
  4. Exit the program
-------------------------------------
"""

#Data
FILE_NAME: str = "Enrollments.csv"


# Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file_obj = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# Read data from CSV file
try:
    with open(FILE_NAME, "r") as file_obj:
        all_rows = file_obj.readlines()
        for row in all_rows:
            row_list = row.strip().split(',')
            students.append({"FirstName": row_list[0], "LastName": row_list[1], "Course": row_list[2]})
except FileNotFoundError as e:
    print("File Not Found")


print(students)

while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        # User input
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the course name: ")
            students.append(
                {"FirstName": student_first_name, "LastName": student_last_name, "Course": course_name}
            )
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")


    elif menu_choice == "2":
        # Current data
        print("\nThe current data is: ")
        print(students)

    elif menu_choice == "3":
        # Process the data to a file
        try:
            file_obj = open(FILE_NAME, "w")
            for student in students:
                file_obj.write(f'{student["FirstName"]},{student["LastName"]},{student["Course"]}' + '\n')
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if not file_obj.closed:
                file_obj.close()


    elif menu_choice == "4":
        # Stop the loop
        print("Program Ended\n")
        sys.exit()

    else:
        print("Please select option 1, 2, 3 or 4")
