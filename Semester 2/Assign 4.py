def employee_list():
    # Indicate this is the initial list
    print("Initial list")
    list = ['Marge Simpson', 'Selma Bouvier', 'Ned Flanders']
    print(list)
    # Add a new employee to the list
    print("\nAdding an employee to the list.")
    list.append('Lenny Leonard')
    print(list)
    print("\nRemoving and Replacing an Employee in the list.")
    try:
        # Replace Ned Flanders with Nelson Muntz
        index = list.index("Ned Flanders")
        list.remove("Ned Flanders")
        list.insert(index, "Nelson Muntz")
        # Print the list
        print(list)
    except:
        # This will trigger if employee (Ned Flanders) is not found in the list
        print("Employee name not found!")
    
    

def main():
    # Call employee list function
    employee_list()

    # Keep the console window open
    input("Program End. Press Enter to exit...")


# Call main function
main()
