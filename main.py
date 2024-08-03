
# This function adds two numbers
def marginal(rate, factor):
    return rate * factor

def factorConvToDecimal(porcent):
    return porcent * 100


while True:
        try:
            rate = float(input("Enter Tax Rate: "))
            factor = float(input("Enter Allocation Factor: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print("Marginal Rate is: ", rate, "*", factor, "=", marginal(rate, factorConvToDecimal(factor)))

        next_calculation = input("Let's do another calc? (yes/no): ")
        if next_calculation == "no":
         break
else:
        print("Invalid Input")