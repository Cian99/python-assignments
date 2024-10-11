def main():
    # Call loop function
    loop()

def details(file_object):
    # Get user to input the details
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    telephone = input("Enter your telephone number: ")
    # Pass these details to the txt function
    txt(file_object, first_name, last_name, telephone)

def txt(file_object, first_name, last_name, telephone):
    # Write the details to the file
    file_object.write("First Name: " + first_name + "\n")
    file_object.write("Last Name: " + last_name + "\n")
    file_object.write("Phone: " + telephone + "\n")
    
def loop():
    # Create txt file to write to
    file_object = open('assign2.txt','w')
    continu = "y"
    # Continue / not
    while continu == "y":
        details(file_object)
        continu = input("Continue? (y = yes): ")
    else:
        print("File Written")
        file_object.close()

# Call main
main()
