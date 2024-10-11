def account_security():
    print("Welcome, please ensure you input the correct account details\n")
    attempts = 0
    # Instructions for the user and attempt counter

    while attempts < 3:
        acc_username = input("Please input username: ")
        acc_password = input("Please input password: ")
        if acc_username == "bank_admin" and acc_password == "Hytu76E":
            print("Welcome", acc_username)
            attempts = 4
    # User enters username and password 
        else:
            print("Incorrect, please try again!\n")
            attempts = attempts + 1
    if attempts ==3:
        print("\nNo attempts remaining")
        print("Security has been contacted!")
    # User only has 3 attempts to enter correct details
    # Otherwise securuity is contacted

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")

def main():
    account_security()


# Call main
main()
    
