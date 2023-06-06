#Global constant to keep program dynamic

#The max number of betting lines
MAX_LINES = 3

#The max number of bets
MAX_BETS = 100

#The min number of bets
MIN_BETS = 1



# Collecting the deposit info from the user
def deposit():
    while True:
        amount = input("How much money you like to despoit? $")

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
            

#Collecting betting information from user

#Getting the number of lines to bet
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        #Checking if the user input is a valid number
        if lines.isdigit():

            #if valid number, convert to int
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")

        else:
            print("Please enter a number.")
        
    return lines

#Getting the amount to bet on each line


#Main function to run the program
def main():
    balance = deposit()
    lines = get_number_of_lines()

    print(balance, lines)

main()
