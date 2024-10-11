def main():
    # Formula for annual sales
    annual_sales = first_quarter + second_quarter + third_quarter + fourth_quarter
    # Display the results
    print("\nACME Sales 2010\n----------")
    print("Quarter 1\t€", first_quarter,".00")
    print("Quarter 2\t€", second_quarter,".00")
    print("Quarter 3\t€", third_quarter,".00")
    print("Quarter 4\t€", fourth_quarter,".00")
    print("Annual Sales\t€", annual_sales,".00")

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")


# Ask user to enter quarterly figures
first_quarter = int(input("Enter first quarter sales figure\t€"))
second_quarter = int(input("Enter second quarter sales figure\t€"))
third_quarter = int(input("Enter third quarter sales figure\t€"))
fourth_quarter = int(input("Enter fourth quarter sales figure\t€"))

# Call the main method
main()
