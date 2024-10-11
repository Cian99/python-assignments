def intro():
    # Introduction to the program for the user
    print("Welcome to the Net Pay Calculator\nFollow the on screen instructions")

def inputs():
    gross_pay = float(input("Enter Gross Pay:\t"))
    main(gross_pay)
    # Gets inputs from user and calls function to calculate net pay 

def main(gross_pay):
    prsi_value = prsi * gross_pay
    health_contribution_value = health_contribution * gross_pay
    paye_value = paye * gross_pay
    usc_value = usc * gross_pay
    net_pay = gross_pay - (prsi_value + health_contribution_value + paye_value + usc_value)
    # Gets correct deduction values from gross pay 
    print("\nGross Pay\t\t€%.2f"% gross_pay)
    print("\nLess Deductions\n----------")
    print("PRSI\t\t\t€%.2f"% prsi_value)
    print("Health Contribution\t€%.2f"% health_contribution_value)
    print("PAYE\t\t\t€%.2f"% paye_value)
    print("U.S.C\t\t\t€%.2f"% usc_value)
    print("\nNet Pay\t\t\t€%.2f"% net_pay)
    # Shows deductions and formatted
    print("Program Complete")

    # Ensure that the user can view results then press enter to close the program
    input("\nPress Enter to exit the program.")


prsi = 0.03
health_contribution = 0.04
paye = 0.41
usc = 0.07
# Deduction percentages in decimal form

# Call the methods           
intro()
inputs()
main()
