# Import random module for random number generation
import random

# Main function - entry point of the program
def main():
    # Call function for user input
    user_input()

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")
    
def user_input():
    # Get the user input
    first_range = int(input("Enter first integer for the range: "))
    second_range = int(input("Enter second integer for the range: "))
    correct_order(first_range, second_range)

# Determine the correct order for the lower and upper bounds of the range
def correct_order(num1, num2):
    if num1 > num2:
        bottom = num2
        top = num1
    else:
        bottom = num1
        top = num2
    random_numbers(bottom, top)

# Generate the 20 random numbers within the range (inclusive)
def random_numbers(bottom, top):
    count = 0
    while count < 20:
        number = random.randint(bottom, top)
        odd_or_even(number)
        count = count + 1

# Check if odd or even
def odd_or_even(number):
    if number % 2 == 0:
        print("Random number", number, "is even")
    else:
        print("Random number", number, "is odd")

main()
