def main():
    # Calculations to perform
    Question_I = A + B * C + D
    Question_II = (A + B) * (C + D)
    Question_III = (A * B) + (C * D)
    Question_IV = A * B + C * D
    Question_V = A * B / C * D
    Question_VI = A * B / (C * D)
    Question_VII = A**B + C**D
    Question_VIII = A**((B + C) * D)

    # Print the results
    print("I. A + B * C + D = ", Question_I)
    print("II. (A + B) * (C + D) = ", Question_II)
    print("III. (A * B) + (C * D) = ", Question_III)
    print("IV. A * B + C * D = ", Question_IV)
    print("V. A * B / C * D = ", Question_V)
    print("VI. A * B / (C * D) = ", Question_VI)
    print("VII. A**B + C**D = ", Question_VII)
    print("VIII. A**((B + C) * D) = ", Question_VIII)

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")

# Ask the user for inputs
A = int(input("Please enter a value for A: "))
B = int(input("Please enter a value for B: "))
C = int(input("Please enter a value for C: "))
D = int(input("Please enter a value for D: "))

# Call the main method
main()




