def main():
    # Initialize the variables
    sum_ = 0
    number = 0
    valid_entries = 0
    invalid_entries = 0
    average = 0

    # Get 5 inputs
    for count in range (5):
        number = int(input("Please enter a number (between 1 and 100):"))

        # Check if valid/not and perform calculations
        if 1 <= number <= 100:
            print("Valid number!")
            sum_ = sum_ + number
            valid_entries = valid_entries + 1
            average = sum_ / valid_entries

        else:
            print("Invalid number!")
            invalid_entries = invalid_entries + 1

    # Print the results
    print("Valid entries: ", valid_entries)
    print("Sum of valid entries: ", sum_)
    print("Average of valid entries: ", average)

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")

# Call the main method
main()
