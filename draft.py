def activity1():
    print("Hello World!")

def activity2():
    name = input("Please enter your name --->  ")

    print("Hi, " + name + ", good afternoon!")

def activity3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")

    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def activity4():
    number1 = eval(input("Enter a number : "))
    number2 = eval(input("Enter another number : "))

    sum = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    reminder = number1 % number2
    floordivision = number1 // number2

    print("The sum of" , number1 , "and" , number2 , "is" , sum)
    print("The difference of" , number1 , "and" , number2 , "is" , difference)
    print("The product of" , number1  , "and" , number2 , "is" , product)
    print("The quotient of" , number1 , "and" , number2 , "is" , quotient)
    print("The exponent of" , number1 , "and" , number2 , "is" , exponent)
    print("The reminder of" , number1 , "and" , number2 , "is" , reminder)
    print("The floor division of" , number1 , "and" , number2 , "is" , floordivision)

def activity5():
    print("FAHRENHEIT TO CELCIUS CONVERTER")

    temp = eval(input("Enter temperature in Fahrenheit: "))

    celsius = (temp - 32) * 5/9

    print(f"The Conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degree celsius.")

def activity6():
    #assignment operator activity

    x = 10

    print(x)

    #how to update the value of x 

    x = x + 2

    print(x)

    #simplified version
    x += 4
    print(x) 

    x += 6
    print(x)

    #other arithmetic
    x -= 8
    print(x)

    #other arithmetic
    x *= 10
    print(x)

    #other arithmetic
    x /= 12
    print(x)

def activity7():
    #conditional statements

    gold = 0

    miner = input("Hi, please enter your name :")

    #answerable by yes or no

    hasMine = input("Did you mine gold today?")

    #introduction to decision structure and relational operators

    if hasMine.lower() == "yes":
        gold += 1
        print(f"Hi, {miner}, today you have a total of {gold} gold.")
    else: 
        print(f"Hi, {miner}, today you have a total of {gold} gold.")

def activity8():
    password = input("Enter your password:  ")

    if password.lower() == "allysakim123":
        print("Your password is correct. Try again.")
        print("Enjoy using the system.")

    elif password.lower() == "password":
        print("Access Granted.")
        print("Enjoy using the system.")

    else :
        print("Your password is incorrect.")

    print("Thank you so much.")

def activity9():
    age = eval(input("Enter your age: "))

    if age >= 1 and age <= 7 :
        print("You are considered Toddler.")
    elif age >= 8 and age <= 13:
        print("You are considered Pre-Teen.")
    elif age >= 14 and age <= 18 :
        print("You are considered Teenager.")
    elif age >= 19 and age <= 31:
        print("You are considered Early Adulthood.")
    elif age >= 32 and age <= 45 :
        print("You are considered Mid Adulthood.")
    elif age >= 46 and age <= 59 :
        print("You are considered Post Adulthood.")
    elif age >= 60 :
        print("You are considered Senior.")
    else :
        print ("Sorry, we cannot find the age you entered. Try again.")

def activity10():
    #create a program for scholarship grant for DLL BSIT student

    isDLL = input("Are you a current student of DLL [yes / no] :  ")

    if isDLL.lower() == "yes" :
        print("Welcome to the DLL Scholarship form. ")

        isPB = input("Are you a resident from Pagbilao? [yes / no] : ")

        if isPB.lower() == "yes" :
            print("Thank you. Now, proceed to the question below. ")

            isLevel = input("What is your current year level at DLL? \nF - Freshman\nSo - Sophomore\nJ - Junior\nS - Senior\nPlease input your answer : ")
            if isLevel.lower() == 'f' :
                print("Welcome, freshman." )
            elif isLevel.lower() == 'sp' :
                print("Welcome, sophomore." )
            elif isLevel.lower() == 'j' :
                print("Welcome, junior." )
            elif isLevel.lower() == 's' :
                print("Welcome, senior.")
            else :
                print("They keyword you input is invalid.")
        else :
            print("Sorry, this scholarship form is only for residents of Pagbilao.")

        isNeeded = input("Do you need this scholarship? [yes / no] : ")
        
        if isNeeded.lower() == "yes" : 
            print("Welcome to this platform. ")
        else : 
            print("Thank you for stopping by. See you next time." )

    else :	
        print("Sorry, this scholarship is only for DLL students.")

def activity11():
    #Print hello world 10 times

    for cycles in range (1, 11):
        print("Hello World!")
        print("Happy Foundation Day.")
        name = input("What is your name? --->  ")
        print(f"Hi, {name}.")

def activity12():
    #starting point is 10
    #stopping point is 1

    for cycle in range (10, 0, -1):
        print(cycle)

def activity13():
    #Factorial

    num = eval(input("Enter a number -->  "))
    factor = 1
    for x in range (num, 0, -1):
        factor *= x

    print(f"The factorial of {num} is {factor}.")

def activity14():
    #washing machine
    #setting

    for x in range (0, 11):
        print(x , end= " ")
        for y in range (0, 11):
            print("<3" , end= " ")
        print()

def activity15():
    for x in range (0 , 20):
        print(x , end= " ")
    for y in range (0 , x):
        print("<3" , end= " ")
    print()

def activity16():
    for x in range (1, 6):
        for y in range (1, x + 1):
            print(" ", end=" ")
        for z in range (6, x, -1):
            print(" * ", end=" ")
        print()

def activity17():
    c = eval(input("Enter number of columns:  "))

    for x in range (1, 11):
        for y in range (1, c + 1):
            print(f"{x} x {y} = {x*y}", end=" \t")
        print()

def activity18():
    tri = eval(input("Enter number of triangles:  "))
    
    for a in range (1, 5):
        for b in range (1, tri + 1):
            for c in range (1, a + 1):
                print("*", end=" ")
            for d in range (5, a, -1):
                print(" ", end=" ")
        print()

def activity19():
        #boolean variable/trigger
        cont = True

        #keyword while
        while cont == True:
            name = input("Enter a name: ")

        #stopping point
            if name.lower() == "stop":
                print("Program Terminated")
                break
                cont = False
            else :
                continue

def activity20():
    import os
    isProceed = True 
    no = 0
    
    while isProceed == True:
        ask = input("Would you like to add another triangle? (yes/no) --->  ")
    
        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isProceed = False
        else:
            os.system("cls")
            no += 1
            for a in range(1, 5):
                for b in range(1, no + 1):
                    for c in range(1, b + 1):
                        print("*", end = " ")
                    for d in range(5, b, -1):
                        print(" ", end=" ")
                print()
            continue

def activity21():
    def func_goodmorning():
        print("Good morning!")

    def func_goodmorning_v2(name):
        print(f"Good morning, {name}")

    def activity13():
        #Factorial

        num = eval(input("Enter a number -->  "))
        factor = 1
        for x in range (num, 0, -1):
            factor *= x
        print(f"The factorial of {num} is {factor}.")

    tuloy = True

    while tuloy == True:
        ask = input("Enter a name:  ")

        if ask.lower() != "stop":
            func_goodmorning_v2(ask)
            if ask == "13":
                activity13()
            continue

        else:
            break

def activity22():
    #name listing and then count names
    loop = True
    names = []
    while loop == True:
        Name = input("What name would you like to add? ")
        if Name.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names! ")
            break
        else:
            names.append(Name)

def activity23():
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"The factorial of 12 is {factorial(12)}.")

def activity24():
    from Activity23_sample import factorial

    print(f"The factorial of 12 is {factorial(12)}. ")

def activity25():
    #python list
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

def code_challenge1():
    print("\t\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t\t*")

def code_challenge2():
    name = input("What is your name:")

    print("\t\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t\t ","Hi !", name ,"\t\t\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t\t*")

def code_challenge3():
    fullname = input("Enter your fullname:")
    age = input("Enter your age:")
    birthmonth = input("Enter your birthmonth:")
    birthday = input("Enter your birthday:")
    birthyear = input("Enter your birthyear:")
    birthplace = input("Enter your birthplace:")
    address = input("Enter your address:")
    citizenship = input("Enter your citizenship:")
    status = input("Enter your status:")

    print("Hi ! , My name is " + fullname + " and I'm "+ age + " years old. I was born on " , birthmonth , birthday , birthyear , " in " , birthplace ,". I lived in " + address +". I'm a " + citizenship + " and I'm " , status+ ".")

def code_challenge4():
    number1 = eval(input("Enter the first number:"))
    number2 = eval(input("Enter another number:"))

    sum = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    reminder = number1 % number2
    floordivision = number1 // number2

    print("The sum of" , number1 , "and" , number2 , "is" , sum)
    print("The difference of" , number1 , "and" , number2 , "is" , difference)
    print("The product of" , number1 , "and" , number2 , "is" , product)
    print("The quotient of" , number1 , "and" , number2 , "is" , quotient)
    print(number1 , "exponent by" , number2 , "is" , exponent)
    print("The reminder of" , number1 , "and", number2 , "is" , reminder)
    print("The floor division of" , number1 , "and" , number2 , "is" , floordivision)

def code_challenge5():
    pera = eval(input("Enter amount to deposit:"))
    print("-------------------------------------")

    libo = pera // 1000
    libo_sukli = pera - (libo * 1000)
    five_h = libo_sukli // 500
    fiveh_sukli = libo_sukli - (five_h * 500)
    two_h = fiveh_sukli // 200
    twoh_sukli = fiveh_sukli - (two_h * 200)
    one_h = twoh_sukli // 100
    oneh_sukli = twoh_sukli - (one_h * 100)
    fifty = oneh_sukli // 50
    fifty_sukli = oneh_sukli - (fifty * 50)
    twenty = fifty_sukli // 20
    twenty_sukli = fifty_sukli - (twenty * 20)
    ten = twenty_sukli // 10
    ten_sukli = twenty_sukli - (ten * 10)
    five = ten_sukli // 5
    five_sukli = ten_sukli - (five * 5)
    one = five_sukli // 1
    one_sukli = five_sukli - (one * 1)

    print(libo , "- 1000")
    print(five_h , "- 500")
    print(two_h , "- 200")
    print(one_h , "- 100")
    print(fifty , "- 50")
    print(twenty , "- 20")
    print(ten , "- 10")
    print(five , "- 5")
    print(one , "- 1")

def code_challenge6():
    #compute final grades

    prelim = eval(input("Prelim Grade ---> "))
    midterm = eval(input("Midterm Grade ---> "))
    semis = eval(input("Semi-Finals Grade ---> "))
    finals = eval(input("Finals Grade ---> "))
    quiz = eval(input("Quiz Grade ---> "))
    project = eval(input("Project Grade ---> "))

    #Nested Condition 
    if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semis >= 65 and semis <= 100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
        FG = (prelim * 0.15) + (midterm * 0.15) + (semis * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15) 
        if FG >= 75 :
            print ("Congratulations, you passed the course/subject.")
        else :
            print("Sorry, you failed. Better luck next time.")
    else : 
        print("The grade is invalid.")

def code_challenge7():
    #grocery
    nameCustomer = input("Enter the customer's name :  ")
    ageCustomer = eval(input("Enter the customer's age : "))
    dGrocery = input("Did you buy a grocery? [yes/no] : ")

    if dGrocery.lower() == "yes":
        print("\n\t\t\tWelcome, enjoy buying groceries!")
        item = input("What item did you buy? :  ")
        price_item = float(input("How much is the item? :   "))
        money = float(input("How much do you like to pay? :   "))
        
        if ageCustomer >= 60:
            taxed = price_item + (price_item * 0.123)
            total = taxed
            change = money - total
            discount = taxed * 0.052
            isDiscounted = total - discount
            changeD = money - isDiscounted 
            print("You can have senior discount of 5.2% from the total price." )
            print(f"Hi, {nameCustomer}, you purchased {item} with the a price of {price_item} plus 12.3% taxed {taxed} minus 5.2% total discount. \nTotal : {isDiscounted} \nAmount Given : {money} \nChange : {round(changeD,2)}")
            
        elif ageCustomer <= 59:
            taxed = price_item + (price_item * 0.123)
            total = taxed
            change = money - total
            print("You are ineligible for the senior discount.")
            print(f"Hi, {nameCustomer}, you purchased {item} with the price of {price_item} plus 12.3% tax {taxed}. \nTotal : {total} \nAmount Given: {money} \nChange : {round(change,2)}")
    else:
        print("Thank you for coming! ")

def code_challenge8():
    #fetch 10 numbers from the users
    #get the summation of all the numbers

    odd = 0
    even = 0
    sum = 0
    for x in range (1, 11):
        num = eval(input(f"Enter #{x} :"))
        sum += num
        if num % 2 == 0:
            even += num
        else:
            odd += num

    print(f"The sum of all the numbers given is {sum}.")
    print(f"The sum of all the odd numbers given is {odd}.")
    print(f"The sum of all the even numbers given is {even}.")

def code_challenge9():
    n = eval(input("enter any number --- >  "))

    for r in range(n,0,-1):
        for i in range(n,r,-1):
            print(" ",end=" ")
        print("* "* r)

def code_challenge10():
    #arrow head up
    for x in range (1, 6):
        for y in range (6, x, -1):
            print(" ", end=" ")
        for z in range (1, x + 1):
            print("*", end=" ")
        for a in range(1, x + 1):
            print("*", end=" ")    
        print()
    #arrow down
    for x in range (1, 6):
        for y in range (1, x + 1):
            print(" ", end=" ")
        for z in range (6, x, -1):
            print("*", end=" ")
        for a in range(6, x, -1):
            print("*", end=" ")    
        print()

def code_challenge11():
    #arrow up
    for x in range (1, 5):
        for y in range(5, x, -1):
            print(" ", end=" ")
        for z in range (1, x):
            print("*", end=" ")
        for a in range (0, x):
            print("*", end=" ")
        print()

    #arrow down
    for x in range (1, 6):
        for y in range (1, x):
            print(" ", end=" ")
        for z in range (6, x, -1):
            print("*", end=" ")
        for a in range (5, x, -1):
            print("*", end=" ")    
        print()

def code_challenge12():
    for x in range (1, 5):
        for y in range(5, x, -1):
            print(" ", end=" ")
        for z in range (1, x):
            print("*", end=" ")
        for a in range (0, x):
            print("*", end=" ")
        print()

    for i in range (x):
        for j in range (x-1):
            print(" ", end=" ")
        print("* * *")

def code_challenge13():
    for x in range (1, 7):
        for y in range (6, x, -1):
            print(" ", end=" ")
        for z in range (x, 1, -1):
            print(z, end=" ")
        for a in range (1, x + 1):
            print(a, end=" ")
        print()

    for x in range (5, 0, -1):
        for y in range (6, x, -1):
            print(" ", end=" ")
        for z in range (x, 1, -1):
            print(z, end=" ")
        for a in range (1, x + 1):
            print(a, end=" ")
        print()

def code_challenge14():
    cont = True
    x = 0

    while cont == True: 
        num = eval(input("Enter a number: "))
        if num == 0:
            print("Program Terminated")
            print(f"The total of the numbers you enter is {x}.")
            break
        else:
            x += num 
            continue

def code_challenge15():
    #HYBRID LOOP

    import os
    isProceed = True
    a = 0
    while isProceed == True:
        question = input("Do you want to add more triangles? (yes/no) :  ")
        
        if question.lower() == "no":
            os.system("cls")
            print("Program Terminated")
            break
            isProceed = False
        elif question.lower() == "yes":
            os.system("cls")
            a += 1
            for x in range (1, 6):
                for y in range (1, a + 1):
                    for z in range (1, x + 1):
                        print("*", end=" ")
                    for q in range (6, x, -1):
                        print(" ", end=" ")
                print()
            continue
        else :
            print("Invalid input, the answer should be yes or no only.")
            continue

def code_challenge16():
    def denomination(amount):
        print("\nDenomination Breakdown:")
        oneth = amount // 1000
        oneth_2 = amount % 1000

        fiveh = oneth_2 // 500
        fiveh_2 = oneth_2 % 500

        twoh = fiveh_2 // 200
        twoh_2 = fiveh_2 % 200

        oneh = twoh_2 // 100
        oneh_2 = twoh_2 % 100

        fifty = oneh_2 // 50
        fifty_2 = oneh_2 % 50

        twenty = fifty_2 // 20
        twenty_2 = fifty_2 % 20

        ten = twenty_2 // 10
        ten_2 = twenty_2 % 10

        five = ten_2 // 5
        five_2 = ten_2 % 5

        one = five_2 // 1

        print("1000---", oneth)
        print("500----", fiveh)
        print("200----", twoh)
        print("100----", oneh)
        print("50-----", fifty)
        print("20-----", twenty)
        print("10-----", ten)
        print("5------", five)
        print("1------", one)


    accounts = {}

    def create_account():
        username = input("Enter your username:  ")
        if username in accounts:
            print("Account already exists!")
        else:
            accounts[username] = 0
            print(f"Account created successfully for {username}.")


    def deposit():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to deposit :   "))
                if amount > 0:
                    accounts[username] += amount
                    print(f"You deposited {amount} successfully. New balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amount <= accounts[username]:
                    accounts[username] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        username = input("Enter your username: ")
        if username in accounts:
            print(f"Your balance: {accounts[username]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("WELCOME TO MY BANK SIMULATION PROGRAM")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose in option 1-5:   ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                print("Thank you for using our Banking System!")
                break
            else:
                print("Invalid option. Please try again.")

import sys
def main():
    """This the main menu of this program"""
    print("\n\t\t\t\t\t ---------- MAIN MENU ---------- ")
    print("\n\t\t\t\tWelcome to my final project. Have fun navigating my program.")
    print("\n1. Topics \n2. Activities \n3. Code Challenge \n4. Exit")

    cont = True
    while cont == True :
        pili = input("Please enter the choice you want to run [Topics, Activities, Code Challenges, Exit]:  ")

        if pili == "1":
            topics_menu()
            main()
        if pili == "2":
            activities_menu()
            main()
        if pili == "3":
            code_challenge_menu()
            main()
        if pili == "4":
            print("Program Terminated")
            sys.exit()
            

def topics_menu():
    tuloy = True

    while tuloy == True:
        print("\n\t\t\t\t\t ---------- Topics ---------- ")
        print("1. Python Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditional Statements")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        break

    tops = input("Enter a topic you want to open [1 - 7]: ")

    if tops == "1":
        python_statements()
    elif tops == "2":
        variables()
    elif tops == "3":
        operators()
    elif tops == "4":
        conditional_statements()
    elif tops == "5":
        loop()
    elif tops == "6":
        python_list()
    elif tops == "7":
        functions()
    elif tops.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        print("Type 'zero' to return to Main Menu.")

def python_statements():
    print("\n------------- PYTHON STATEMENTS ------------")
    print("The python statement is an instruction that the python interpreter can execute. ")
    print("\n---------------------------------------------")
    print("\n Example: [ACTIVITY 1]")

    ques = input("Would you like to open the code example [activity 1]? yes or no : ")
    if ques.lower() == "yes":
        print("\nOutput:")
        activity1()
    elif ques.lower() == "zero":
        main()

    else:
        print("Invalid Choice.")
        python_statements()

def variables():
    print("\n ------------ VARIABLES ------------")
    print("\nThe variables are containers for storing data values.")
    print("\n---------------------------------------------")
    print("\nExample: [CODE CHALLENGE 3]")

    ques = input("Would you like to open the code example [code challenge 3]? yes or no : ")
    if ques.lower() == "yes":
        code_challenge3()
    elif ques.lower() == "zero":
        main()

    else:
        print("Invalid Choice.")
        variables()

def operators():
    print("\n ------------ OPERATORS ------------")
    print("\nThe operators are used to perform operations on variables and values.")
    print("\n---------------------------------------------")
    print("\nExample: [CODE CHALLENGE 4]")

    ques = input("Would you like to open the code example [code challenge 4]? yes or no : ")
    if ques.lower() == "yes":
        code_challenge4()
    elif ques.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        operators()

def conditional_statements():
    print("\n ------------ CONDITIONAL STATEMENTS ------------")
    print("\nThe conditional statements are used to execute a specific block of code based on the truth value of a condition.")
    print("\n---------------------------------------------")
    print("\nExample: [ACTIVITY 10]")

    ques = input("Would you like to open the code example [activity 10]? yes or no : ")
    if ques.lower() == "yes":
        activity10()
    elif ques.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        conditional_statements()

def loop():
    print("\n ------------ LOOP ------------")
    print("\nThe loop is a control flow statement that is used repeatedly execute a group of statements as long as the condition is satisfied .")
    print("\n---------------------------------------------")
    print("\nExample: [ACTIVITY 20]")

    ques = input("Would you like to open the code example [activity 20]? yes or no : ")
    if ques.lower() == "yes":
        activity20()
    elif ques.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        loop()

def python_list():
    print("\n ------------ PYTHON LISTS ------------")
    print("\nThe python lists are used to store multiple items in a single variable.")
    print("\n---------------------------------------------")
    print("\nExample: [ACTIVITY 25]")

    ques = input("Would you like to open the code example [activity 25]? yes or no : ")
    if ques.lower() == "yes":
        activity25()
    elif ques.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        python_list()

def functions():
    print("\n ------------ FUNCTIONS ------------")
    print("\nThe functions is a block of code which only runs when it is called.")
    print("\n---------------------------------------------")
    print("\nExample: [CODE CHALLENGE 16]")

    ques = input("Would you like to open the code example [code challenge 16]? yes or no : ")
    if ques.lower() == "yes":
        code_challenge16()
    elif ques.lower() == "zero":
        main()

    else:
        print("Program Terminated")
        functions()

import os

def activities_menu():
    tuloy = True

    while tuloy == True:
        print("\n\t\t\t\t\t======================= Activities =====================")
        print("\t\t\t\t\t|| A1 - Activity 1                       A14 - Activity 14 ||")
        print("\t\t\t\t\t|| A2 - Activity 2                       A15 - Activity 15 ||")
        print("\t\t\t\t\t|| A3 - Activity 3                       A16 - Activity 16 ||")
        print("\t\t\t\t\t|| A4 - Activity 4                       A17 - Activity 17 ||")
        print("\t\t\t\t\t|| A5 - Activity 5                       A18 - Activity 18 ||")
        print("\t\t\t\t\t|| A6 - Activity 6                       A19 - Activity 19 ||")
        print("\t\t\t\t\t|| A7 - Activity 7                       A20 - Activity 20 ||")
        print("\t\t\t\t\t|| A8 - Activity 8                       A21 - Activity 21 ||")
        print("\t\t\t\t\t|| A9 - Activity 9                       A22 - Activity 22 ||")
        print("\t\t\t\t\t|| A10 - Activity 10                     A23 - Activity 23 ||")
        print("\t\t\t\t\t|| A11 - Activity 11                     A24 - Activity 24 ||")
        print("\t\t\t\t\t|| A12 - Activity 12                     A25 - Activity 25 ||")
        print("\t\t\t\t\t================================================================\n")
        
        code = input("Enter an activity you want to run [1 - 25]:  ")

        if code.lower() == "a1":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 1")
                activity1()
                print("\n================================================================================")
                continue
                
        elif code.lower() == "a2":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 2")
                activity2()
                print("\n================================================================================")
                continue

        elif code.lower() == "a3":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 3")
                activity3()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a4":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 4")
                activity4()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a5":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 5")
                activity5()
                print("\n================================================================================")
                continue

        elif code.lower() == "a6":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 6")
                activity6()
                print("\n================================================================================")
                continue

        elif code.lower() == "a7":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 7")
                activity7()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a8":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 8")
                activity8()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a9":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 9")
                activity9()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a10":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 10")
                activity10()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a11":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 11")
                activity11()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a12":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 12")
                activity12()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a13":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 13")
                activity13()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a14":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 14")
                activity14()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a15":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 15")
                activity15()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a16":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 16")
                activity16()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a17":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 17")
                activity17()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a18":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 18")
                activity18()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a19":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 19")
                activity19()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a20":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 20")
                activity20()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a21":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 21")
                activity21()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a22":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 22")
                activity22()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a23":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 23")
                activity23()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a24":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 24")
                activity24()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a25":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 25")
                activity25()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "zero":
            main()
            
        else:
            print("Invalid Choice.")
            print("Type 'zero' to back to Main Menu.")

def code_challenge_menu():
    tuloy = True

    while tuloy == True:
        print("\t\t\t\t\t=====================| Code Challenge |==========================")
        print("\t\t\t\t\t|| CC1 - Code Challenge 1              CC9 - Code Challenge 9   ||")
        print("\t\t\t\t\t|| CC2 - Code Challenge 2              CC10 - Code Challenge 10 ||")
        print("\t\t\t\t\t|| CC3 - Code Challenge 3              CC11 - Code Challenge 11 ||")
        print("\t\t\t\t\t|| CC4 - Code Challenge 4              CC12 - Code Challenge 12 ||")
        print("\t\t\t\t\t|| CC5 - Code Challenge 5              CC13 - Code Challenge 13 ||")
        print("\t\t\t\t\t|| CC6 - Code Challenge 6              CC14 - Code Challenge 14 ||")
        print("\t\t\t\t\t|| CC7 - Code Challenge 7              CC15 - Code Challenge 15 ||")
        print("\t\t\t\t\t|| CC8 - Code Challenge 8              CC16 - Code Challenge 16 ||")
        print("\t\t\t\t\t\t\t\t\T 0 - Exit")
        print("\t\t\t\t\t================================================================")

        code = input("\nEnter a code challenge you want to run [1 - 16]: ")
                
        if code.lower() == "cc1":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 1")
            code_challenge1()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc2":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 2")
            code_challenge2()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc3":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 3")
            code_challenge3()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc4":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 4")
            code_challenge4()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc5":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 5")
            code_challenge5()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc6":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 6")
            code_challenge6()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc7":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 7")
            code_challenge7()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc8":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 8")
            code_challenge8()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc9":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 9")
            code_challenge9()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc10":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 10")
            code_challenge10()
            print("\n================================================================================")
            continue

        elif code.lower() == "cc11":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 11")
            code_challenge11()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc12":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 12")
            code_challenge12()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc13":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 13")
            code_challenge13()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc14":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 14")
            code_challenge14()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc15":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 15")
            code_challenge15()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc16":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 16")
            code_challenge16()
            print("\n================================================================================")
            continue

        elif code.lower() == "zero":
            main()

        else:
            print("Invalid Choice.")
            print("Type 'zero' to return to Main Menu.")
            main()
main()



















