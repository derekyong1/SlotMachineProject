# Collecting the deposit info from the user
def deposit():
    while True:
        amount = input("How would you like to despoit? $")

        #Checking if the user input is a valid number
        if amount.isdigit():

            #if valid number, convert to int
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number.")
            
    return amount
            
deposit()


