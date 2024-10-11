def main():
    # Get name for the file from user
    name = input("Please enter a file name: ")
    # Display menu options
    print("Choose a number to continue:")
    print("Select 1 to create a file ")
    print("Select 2 to read a file ")
    print("Select 3 to append to a file ")
    print("Select 4 to calculate total of file ")
    print("Select 5 to exit program ")
    # Get and process the user input
    number = input("Enter menu choice: ")
    if number == '1':
        filecreate(name)
    elif number == '2':
        outputtoscreen(name)
    elif number == '3':
        appendtofile(name)
    elif number == '4':
        totalnumbers(name)
    elif number == '5':
        print("Exiting the program.")
    else:
        print("Invalid choice!")

    # Keep the console window open
    input("Program End. Press Enter to exit...")

# Create a file and write numbers to it
def filecreate(name):
    # Set the initial condition
    continu = "Y"
    # Open file in write mode
    file_object = open(name, 'w')
    while continu == "Y":
        # Take user numbers while continue is yes
        number = input("Please enter a number to be printed to the file: ")
        file_object.write(number + '\n') # Write the number to the file
        continu = input("Continue? (Y = Yes) ")
    file_object.close() # Close the file
    return name

# Read and display contents of the file
def outputtoscreen(name):
    # Open file in read mode and read the contents
    file_object = open(name, 'r')
    file_contents = file_object.read()
    # Print the contents and close the file
    print ("File contents:\n", file_contents)
    file_object.close()

# Append numbers to existing file
def appendtofile(name):
    # Set the initial condition
    appending = "Y"
    # Open file in append mode
    file_object = open(name, 'a')
    while appending == "Y":
        # Take user numbers while continue is yes and write to file
        number = input("Append:\nPlease enter a number to be printed to the file: ")
        file_object.write(number + '\n')
        appending = input("Continue? (Y = Yes) ")
    file_object.close()

# Calculate total of all numbers in the file
def totalnumbers(name):
    # Initialize variable to store the total
    total = 0
    # Open file in read mode
    file_object = open(name, "r")
    # Loop through the file
    for line in file_object:
        # Convert each line to an integer and add to total
        total += (int (line))
    # Print the sum
    print("Sum of file contents: ", total)
    file_object.close()


# Call the main function
main()
