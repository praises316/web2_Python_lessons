print('''
This simple ATM machine I built with Python will allow users do the following:

1. Check their balance
2. Deposit money
3. Withdraw money
4. Exit the program
''')

# The line below defines a dictionary named bank_account to simulate a user's bank account.

bank_account = {
    "account_balance": 1000,  # Initial balance
    "account_pin": 1020       # PIN for the bank_account
}

print(bank_account)
print(bank_account["account_balance"])
print(bank_account["account_pin"])

# This line shows the bank_account menu for the user to select an option of what they want to do.
def show_menu():
    print("Welcome to Zen's ATM\n")
    print("1. To check your balance")
    print("2. To deposit money")
    print("3. To withdraw money")
    print("4. Exit")
    your_choice = input("Please pick an option within (1-4): ")
    return your_choice

# This line prints the current balance of the user's bank account
def check_account_balance():
    print(f"Your current account balance is: #{bank_account['account_balance']}")

# This line allows the user to deposit money into the bank account
def deposit_money():
    amount = float(input("Enter any amount to deposit: "))
    if amount > 0:
        bank_account["account_balance"] += amount
        print(f"#{amount} has been deposited to your account. Your new account balance is: #{bank_account['account_balance']}")
    else:
        print("Invalid amount!!! \nPlease enter a positive number.")

# This line allows the user to withdraw money from the bank account
def withdraw_money():
    amount = float(input("Enter the amount you wish to withdraw: "))
    if amount > 0:
        if amount <= bank_account["account_balance"]:
            bank_account["account_balance"] -= amount
            print(f"#{amount} has been withdrawn. Your new account balance is: #{bank_account['account_balance']}")
        else:
            print("Insufficient funds!")
    else:
        print("Invalid amount!!! \nPlease enter a positive number.")

# This line runs the ATM program by allowing the user to enter a PIN which then displays the ATM's main menu
def run_zens_atm():
    account_pin = input("Please enter your PIN to proceed: ")

    if account_pin == str(bank_account["account_pin"]):
        while True:
            your_choice = show_menu()
            if your_choice == "1":
                check_account_balance()
            elif your_choice == "2":
                deposit_money()
            elif your_choice == "3":
                withdraw_money()
            elif your_choice == "4":
                print("Thank you for using Zen's ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option within (1-4).")
    else:
        print("Incorrect PIN. Please try again.")

# Start the program
run_zens_atm()

