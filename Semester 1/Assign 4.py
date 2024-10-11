discount1 = 0.00
discount2 = 0.06
discount3 = 0.12
discount4 = 0.20
dog_food_price = 6.75
# Discount percentages and cost per bag of dog food

def instructions():
    print("Welcome, please enter the password")
    # Instructions function

def discount():
    print("Please enter the number of bags of dog food purchased")
    dog_food_bags = float(input("Bags of dog food: "))
    price = dog_food_bags * dog_food_price
    if dog_food_bags < 20:
        discount = price * discount1
        print("Total Cost: €", price)
        print("0% discount = €", discount)
        final_price = price - discount
        print("Final Price: €", final_price)
    elif 20 <= dog_food_bags <=79:
        discount = price * discount2
        print("Total Cost: €", price)
        print("6% discount = €", discount)
        final_price = price - discount
        print("Final Price: €", final_price)
    elif 80 <= dog_food_bags <=109:
        discount = price * discount3
        print("Total Cost: €", price)
        print("12% discount = €", discount)
        final_price = price - discount
        print("Final Price: €", final_price)
    elif dog_food_bags >= 110:
        discount = price * discount4
        print("Total Cost: €", price)
        print("20% discount = €", discount)
        final_price = price - discount
        print("Final Price: €", final_price)
    # This function calculates the discount by reading in the number of bags

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")

def password():
    password = input("Password: ")
    if password == "QWERTY":
        discount()
    else:
        print("Incorrect Password! Try Again")
        main()
    # Checks password is correct before applying the discount

def main():
    # Call the other functions
    instructions()
    password()


# Call main
main()
