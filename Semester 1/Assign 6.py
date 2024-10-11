def loop_while():
    print("The sum of the numbers from 1 to 100 inclusive using a while loop is:")
    total = 0
    number = 1

    while number <= 100:
        total = total + number
        number = number + 1
    print(total)

def loop_for():
    print("\nThe sum of the numbers from 1 to 100 inclusive using a for loop is:")
    total = 0

    for x in range(1,101):
        total = total + x

    print(total)

def main():
    print("Welcome! This program displays the sum of 1 to 100 inclusive\n")
    loop_while()
    loop_for()

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")
    

# Call main
main()
