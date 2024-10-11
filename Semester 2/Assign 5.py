def two_d_list():
    # Create list and ask user for inputs (number of students and grades per)
    list_overall = list()
    num_students = int(input("Number of Students to enter: "))
    num_grades = int(input("Number of Grades per student: "))
    # Iterate through the list of students, adding the data
    for r in range(num_students):
        mini_list = list()
        ID = input("Enter Student ID number: ")
        mini_list.append(ID)
        list_overall.append(mini_list)

        # Nested loop
        # Iterate through each students list of grades, adding the data
        for c in range(num_grades):
            grade = input("Enter Grade for module: ")
            mini_list.append(grade)
        

    # Print and format the results
    print("Student List:\n",list_overall)
    print("\nRows and Columns:")
    for a in list_overall:
        for elem in a:
            print("{}".format(elem).rjust(3), end="")
        print(end="\n")

def main():
    # Call the 2d list function
    two_d_list()

    # Keep the console window open
    input("Program End. Press Enter to exit...")


# Call main function
main()
