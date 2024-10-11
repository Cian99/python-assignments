def initials():
    # Get user to enter their name
    name = str(input("Enter your full name: "))
    # Separate the first and last name
    name_list = name.split()

    # Find the first letter of each component
    for i in name_list:
        print(i[0].upper() + '.', end="")

def main():
    # Call initials funciton
    initials()

    # Keep the console window open
    input("\nProgram End. Press Enter to exit...")


# Call main function
main()
