def denomination(amount):
        print("\nDenomination Breakdown:")
        TH = amount // 1000
        THSUKLI = amount % 1000

        FH = THSUKLI // 500
        FHSUKLI = THSUKLI % 500

        TWH = FHSUKLI // 200
        TWHSUKLI = FHSUKLI % 200

        OH = TWHSUKLI // 100
        OHSUKLI = TWHSUKLI % 100

        FI = OHSUKLI // 50
        FISUKLI = OHSUKLI % 50

        TWEN = FISUKLI // 20
        TWENSUKLI = FISUKLI % 20

        TEN = TWENSUKLI // 10
        TENSUKLI = TWENSUKLI % 10

        FIVE = TENSUKLI // 5
        FIVESUKLI = TENSUKLI % 5

        I = FIVESUKLI // 1

        print("1000---", TH)
        print("500----", FH)
        print("200----", TWH)
        print("100----", OH)
        print("50-----", FI)
        print("20-----", TWEN)
        print("10-----", TEN)
        print("5------", FIVE)
        print("1------", I)


accounts = {}

def account():
        x = input("Enter an account name: ")
        if x in accounts:
            print("Account already exists!")
        else:
            accounts[x] = 0
            print(f"Account created successfully for {x}.")


def deposit():
        x = input("Enter your account name: ")
        if x in accounts:
            try:
                amount = int(input("Enter amount to deposit : "))
                if amount > 0:
                    accounts[x] += amount
                    print(f"Deposited {amount} successfully. New balance: {accounts[x]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


def withdrawal():
        x = input("Enter your account name: ")
        if x in accounts:
            try:
                amount = int(input("Enter amount to withdraw : "))
                if 0 < amount <= accounts[x]:
                    accounts[x] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[x]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


def check_balance():
        x = input("Enter your username: ")
        if x in accounts:
            print(f"Your balance: {accounts[x]}")
        else:
            print("Account not found!")


def options():
        while True:
            print("Welcome to my Simulation Bank")
            print()
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            print()
            y = input("Choose an option: ")
            print()

            if y == '1':
                account()
            elif y == '2':
                deposit()
            elif y == '3':
                withdrawal()
            elif y == '4':
                check_balance()
            elif y == '5' or "Exit":
                print("Transaction ended ")
                break
            else:
                print("Invalid option. Please try again.")
options()