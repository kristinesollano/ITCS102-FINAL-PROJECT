def Activity1():
    print('\nHELLO WORLD!')

def Activity2():
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter a number: "))
    answer = num1 + num2

    print(num1, "+" ,num2, "=" ,answer,)

def Activity3():
    num1 = eval(input("Please enter the first number: "))
    num2 = eval(input("Please enter the first number: "))
    result = num1 + num2

    print(result)

def Activity4():
    number1 = int(input("Enter a number - - - > "))
    number2 = int(input("Enter another number - - - > "))

    add = number1 + number2
    product = number1 * number2
    minus = number1 - number2
    quotient = number1 / number2
    exponent = number1 ** number2
    remainder = number1 % number2
    floor = number1 // number2

    print("The sum of" ,number1 , " and " , number2 , " is " , add)
    print("The product of" ,number1 , " and " , number2 , " is " , product)
    print("The difference of" ,number1 , " and " , number2 , " is " , minus)
    print("The quotient of" ,number1 , " and " , number2 , " is " , quotient)
    print("The exponent of" ,number1 , " and " , number2 , " is " , exponent)
    print("The remainder of" ,number1 , " and " , number2 , " is " , remainder)
    print("The floor division of" ,number1 , " and " , number2 , " is " , floor)

def Activity5():
    print("FAHRENHEIT TO CELCIUS CONVERTER")

    temp = eval(input("Enter temperature in Fahrenheit : "))

    celsius = (temp - 32) * 5 / 9

    print("The Conversion of ", temp , "degrees Fahrenheit is ", celsius , "degrees celcius. ")

    print(f"The conversion of {temp} degress Fahrenheit is {celsius} degrees celcius")

    print(round(celsius, 2))

def Activity6():
    x = 5

    print(x)

    x = x+ 5

    print(x)

    x = x+10

    print(x)

    x = x+35

    print(x)

    x = x-25

    print(x)

def Activity7():
    gold = 0

    miner = input("Hi, please enter your name - - - > ")

    #answerable by yes or no

    hasMine = input("Do you have a gold ? ")

    if hasMine.lower () == "yes":
        gold += 10
        print(f"Please {miner}, you probably doesn't have a gold. I'll give you {gold} gold ")

    else:
        print(f"Please {miner}, you probably doesn't have a gold. I'll give you {gold} gold ")


def Activity8():
    password = input("Enter your password - - - > ")

    if password.lower() == "secret" :
        print("Acess Granted")
        print("Enjoy using the system")

    elif password == "hello world":
        print("Acess Granted")
        print("Enjoy using the system")

    else:
        print("Acess Denied")

    print("Thank you for using the system")

def Activity9():
    age = eval(input("Enter your age - - - > "))

    if age >= 1 and age <= 7:
        print("toddler ")

    elif age >= 8 and age <= 13:
        print("pre teen ")

    elif age >= 14 and age  <= 18:
        print("teenager")

    elif age >= 19 and age  <= 31:
        print("early adulthood")

    elif age >= 32 and age  <= 45:
        print("mid adulthood")

    elif age >= 46 and age <= 59:
        print("post adulthood")

    elif age >= 60:
        print("senior")

    else:
        print("invalid age")

def Activity10():
    isDLL = input("Are you a current student of DLL (yes/no)  : ")

    if isDLL.lower() == "yes": 
        print("Welcome to the DLL BSIT scholarship!")
        isGG = input("Are you from Brgy. Gulang-gulang (yes/no) :")

        if isGG.lower() == "yes" :
            print("Please fill up the second form ")
            islevel = input("What is your current year level right now in DLL\nF - Freshman\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer: ")

            if islevel . lower ( ) == "f" :
                print("Hi, Freshman!" )
            elif islevel . lower ( ) == "s" :
                print("Hi, Sophomore!" )
            elif islevel . lower ( ) == "j" :
                print("Hi, Junior!" )
            elif islevel . lower ( ) == "r" :
                print("Hi, Senior!" )
            else :
                print("Invalid choice")

            isNeeded = input("Do you need this Scholarship (yes/no) : ")
        
            if isNeeded.lower() == "yes" :
                print("Scholarship Granted! ")
            else :
                print("Thank you for stopping by! ")
                
        else :
            print("Sorry, this Scholarship are only given from the resident of Gulang-gulang")
    else :
            print("Thank you for stopping by! ")

def Activity11():
    for apple in range(1, 51):
        print("hello, good morning")
    name = input("Whats your name: ")
    print(f"Hi, {name}")

def Activity12():
    for x in range(10, 0, -1):
        print(x)

def Activity13():
    num = eval(input("Enter any number: "))
    factorial = 1

    for abc in range(num, 0, -1):
        factorial *= abc

    print(f"The factorial of {num} is {factorial} ")

def Activity14():
    for k in range(0, 11):
        print(k, end = " ")

    for z in range(0, 11):
        print("*", end = " ")
    print()

def Activity15():
    for i in range(0,21):
        print(i,end = " ")
    for t in range(0,i):
        print("*", end=" ")

    print()


def Activity16():
    for x in range(1,6):
        for y in range(1, x + 1):
            print(" ", end =" ")
    for z in range(6, x, -1):
        print("$", end =" ")

    print()


def Activity17():
    col = eval(input("Enter a number of colums ----> "))

    for x in range(1,11):
        for y in range(1, col+1):
            print(f"{x} x {y} = {x*y}", end = "\t")
        print()

def Activity18():
    no = eval(input("Enter a number of triangles ---->"))
    for x in range(1,5):
        for r in range(1,no + 1):
            for y in range(1,x + 1):
                print("*", end= " ")

            for z in range(5, x, -1):
                print(" ", end=" ")
        print()

def Activity19():
    tuloy = True

    while tuloy == True:
        name = input("Please enter a name: ")

        if name.lower() == "stop":
            print("Program Terminated")
            break
            tuloy = False

        else:
            continue

def Activity20():
    import os

    isContinue = True
    no = 0

    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no) ---->")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break

            isContinue = False

        else:
            os.system('cls')
            no += 1
            for x in range(1,5):
                for r in range(1, no + 1):
                    for y in range(1,x, +1):
                        print("*", end=" ")

                    for z in range(5, x, -1):
                        print(" ", end=" ")
                print()
                continue


def Activity21():
    def say_hello():
        print("Hello Sollano")

    def say_hello_v2(name):
        print(f"Hello {name}")

    def activity2():
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter another number: "))
        total = number1 + number2
        print(number1, " plus ", number2, " = ", total)

    tuloy = True
    while tuloy:
        ask = input("Please provide a name: ")

        if ask.lower() != "stop":
            say_hello_v2(ask)
            if ask.lower() == "2":
                activity2()
            continue
        
        else:
            break


def Activity22():
    #Name listing and then count names

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
        fact = 1
        for k in range(number, 0, -1):
            fact *= 1
        return fact

def Activity24():
    from Activity23_sample import factorial
    print(f"The Factorial of 4 is {factorial(4)}")

def Activity25():
    courses = ["BSIT", "BSA", "BSAIS", "BSTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

def Code_challenge1():
    print("\n\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t\b\b***** \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t*")


def Code_challenge2():
    name = input("Enter your name: ")

    print(f"\n\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t\b\b*{name}* \n\t\t\t\t\t\t\t\t\t\t\b*** \n\t\t\t\t\t\t\t\t\t\t*")


def Code_challenge3():
    Name = input("PLEASE INPUT YOUR NAME : ")
                          
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")

    Age = input("PLEASE INPUT YOUR AGE : ")

    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")

    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")

    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")

    Gender = input("PLEASE INPUT YOUR GENDER : ")

    Address = input("PLEASE INPUT YOUR ADDRESS : ")

    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")

    isMarried = False

    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")

    Religion = input("PLEASE INPUT YOUR RELIGION : ")

    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")

    Height = input("PLEASE INPUT YOUR HEIGHT : ")

    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")

    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")

    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")

    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")

    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")

    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")

    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")

    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")

    YearAttendedElementary = input("PLEASE INPUT YOUR YEARATTENDEDELEMENTARY : ")

    YearEndedElementary = input("PLEASE INPUT YOUR YEARENDEDELEMENTARY : ")

    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")

    YearAttendedHighSchool = input("PLEASE INPUT YOUR YEARATTENDEDHIGHSCHOOL : ")

    YearEndedHighSchool = input("PLEASE INPUT YOUR YEARENDEDHIGHSCHOOL : ")

    College = input("PLEASE INPUT YOUR COLLEGE : ")

    Course = input("PLEASE INPUT YOUR COURSE : ")

    Skills = input("PLEASE INPUT YOUR SKILLS : ")


    print("My name is " + Name + ", I am often referred to as " + Nickname + ".\nI am " ,Age, " years old, born in " + Birthmonth + " on " + Birthday + ", " + Birthyear + ".\nI currently reside at " + Address + ".\nI am " + Gender + " by gender and my religion is " + Religion + "." + "\nMy nationality is " + Nationality + ", and I hold " + Citizenship + " citizenship" + ".\nIt is " ,isMarried, "that I am married and my civil status is " + CivilStatus + ".\nMy height is" ,Height, "in cm and I weigh" ,Weight,"in kg." + "\nMy father is " + NameofFather + ", works as a " + OccupationofFather + ".\nHe can be reached at " ,ContactNumberofFather,"\b.\nMy mother name is " + NameofMother + ", is employed as a " + OccupationofMother + "\b.\nShe can be reached at " ,ContactNumberofMother, "\nIn terms of my Educational Background,\nI completed my elementary education at " + Elementary + " from " ,YearAttendedElementary,"to",YearEndedElementary,"\b.\nI then attended High School in " + HighSchool + " from " ,YearAttendedHighSchool,"to",YearEndedHighSchool,"\b.\nI pursued higher education at " + College + ", where I studied " + Course + ".\nI have developed skills in " + Skills + ".\nDeveloping these skills will help me navigate complex situations, enhance my professional growth,\nand contribute more effectively goals.")



def Code_challenge4():
    number1 = eval(input("Enter a number --> "))

    number2 = eval(input("Enter a number --> "))


    answer1 = number1 + number2

    answer2 = number1 - number2

    answer3 = number1 * number2

    answer4 = number1/number2

    answer5 = number1 ** number2

    answer6 = number1 % number2

    answer7 = number1 // number2

    print("The sum of", number1, "and", number2, "is", answer1)

    print("The difference of", number1, "and", number2, "is", answer2)

    print("The product of", number1, "and", number2, "is", answer3)

    print("The quotient of", number1, "and", number2, "is", answer4) 

    print("The exponent by", number1, "and", number2, "is", answer5)

    print("The remainder of", number1, "and", number2, "is", answer6)

    print("The floor division of", number1,"and", number2, "is", answer7)


def Code_challenge5():
    bank_name = input("Please Input your Bank Account Name: ")
    bad = eval(input("Please Enter Amount to Deposit:       "))

    dp1 = bad // 1000
    n1 = bad % 1000
    dp2 = n1 // 500
    n2 = n1 % 500
    dp3 = n2 // 200
    n3 = n2 % 200
    dp4 = n3 // 100
    n4 = n3 % 100
    dp5 = n4 // 50
    n5 = n4 % 50
    dp6 = n5 // 20
    n6 = n5 % 20
    dp7 = n6 // 10
    n7 = n6 % 10
    dp8 = n7 // 5
    n8 = n7 % 5
    dp9 = n8 // 1

    # Define the width for each column
    width = 15

    print('-' * (width * 2))
    print(f"{'Amount':<{width}} | {'          Count':<{width}}")
    print('-' * (width * 2))
    print(f"{'1000':<{width}} |{dp1:>{width}}")
    print('-' * (width * 2))
    print(f"{'500':<{width}} |{dp2:>{width}}")
    print('-' * (width * 2))
    print(f"{'200':<{width}} |{dp3:>{width}}")
    print('-' * (width * 2))
    print(f"{'100':<{width}} |{dp4:>{width}}")
    print('-' * (width * 2))
    print(f"{'50':<{width}} |{dp5:>{width}}")
    print('-' * (width * 2))
    print(f"{'20':<{width}} |{dp6:>{width}}")
    print('-' * (width * 2))
    print(f"{'10':<{width}} |{dp7:>{width}}")
    print('-' * (width * 2))
    print(f"{'5':<{width}} |{dp8:>{width}}")
    print('-' * (width * 2))
    print(f"{'1':<{width}} |{dp9:>{width}}")
    print('-' * (width * 2))


def Code_challenge6():
    prelim = eval(input("Please enter your grades in prelim: "))
    midterm = eval(input("Please enter your grades in midterm: "))
    semi_final = eval(input("Please enter your grades in semi_final: "))
    final = eval(input("Please enter your grades in final: "))
    quiz = eval(input("Please enter your grades in quiz: "))
    project = eval(input("Please enter your grades in project: "))

    finalgrade = (prelim * .15) + (midterm * .15) + (semi_final * .15) + (final * .15) + (quiz * .15) + (project * .15)

    totalgrade = round(finalgrade, 2)

    print(f"Your total grade is {totalgrade}")

    if finalgrade > 100:
        print("INVALID GRADE!")
    elif finalgrade >= 74 and finalgrade <= 100:
        print("Congratulations! You passed the course!")
    else: 
        print("Sorry, you failed!")


def Code_challenge7():
    customer_name = input("Enter the customer's name here: ")
    customer_age = eval(input("Enter the customer's age" ))
    grocery = input("Have you ever done your groceries? (yes/no) ")

    if grocery.lower() == "yes":
        print("Proceed in buying groceries")
        item = input("What is the name of the item: ")
        price = eval(input("What is the price of the item: "))
        payment = eval(input("What is the amount given: "))
        
        if customer_age >= 60:
            total = price + (price * 0.123)
            tax = price * 0.123
            discount = tax * 0.123
            total_discount = total - discount
            discount_change = payment - total_discount
            discount_change = round(discount_change, 3)
            print("Senior discount of 5.2% is being applied from the total price")
            print("Hi {name}, you purchase {item} with a price of {price} plus a 12.3% tax {tax} and a 5.2% senior discount")
            
            print("Total of {discount} \nAmount given: {amount} \nChange: {Change} ")
            
        elif customer_age <= 59:
            total = price + (price * 0.123)
            tax = price * 0.123
            discount_change = payment - total
            discount_change= round(discount_change, 3)
            print(f"Hi {customer_name}, you purchase {item} with a price {price} plus a 12.3% tax {tax}")
                
            print(f"Total of: {total} \nPayment given: {payment} \nChange: {discount_change} ")
                
        else:
            print("Thank you for stopping by! ")


def Code_challenge8():
    odd = 0
    even = 0
    sum = 0

    for abc in range (1,11):
        num = eval(input(f"Enter a number {abc}: "))
        sum += num
        if num % 2 == 0:
            even += num
        else:
            odd += num

    print(f"The sum of all numbers is {sum}")
    print(f"The sum of all numbers is {even}")
    print(f"The sum of all numbers is {odd}")


def Code_challenge9():
    for x in range(11, 0, -1):
        for y in range(x, 0, -1):
            print("*", end = " ")
    print()


def Code_challenge10():
    for x in range(10,1,-1):
        for y in range(x,10):
            print(" ",end=" ")
        for a in range(1,x):
            print("*",end=" ")
            
        print()


def Code_challenge11():
    for l in range(1, 7): 
        for m in range(6, l -1):
            print(" ", end = " " )
    for n in range(l, 1, -1):
        print(n, end=" ")
    for o in range(1, l, +1):
        print(o, end=" ")
   
    print()


def Code_challenge12():
    for x in range(1,10):
        for y in range(x,9):
            print(" ",end=" ")
        for a in range(1,x):
            print("*",end=" ")
        for b in range(0,x):
            print("*",end=" ")
            
        
        print()    
        
        

    for x in range(1,11):
        for y in range(1,7):
            print(" ",end=" ")
        for y in range(1,6):
            print("*",end=" ")    
        print()


def Code_challenge13():
    for x in range(1,7):
        for y in range(6,x,-1):
            print(" ",end=" ")
        for y in range(x,1,-1):
            print(y,end=" ")
        for b in range(1,x+1):
            print(b,end=" ")
            
        
        print()    
        
        

    for x in range(5,0,-1):
        for y in range(6,x,-1):
            print(" ",end=" ")
        for y in range(x,1,-1):
            print(y ,end=" ")
        for a in range(1,x+1):
            print(a,end=" ")
        print()


def Code_challenge14():
    isLoop = True
    number = 0

    while isLoop == True:
        apple = eval(input("Enter a number> "))
        if apple > 0:
            number += isLoop
            continue
        elif apple == 0:
            print("Loop has been terminated.")
            print(f"the sum of all the numbers given is {number}")
            break
            isLoop = False
        else:
            print("Please enter a number.")
            continue


def Code_challenge15():
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


def Code_challenge16():
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
        Activity1()
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
        Code_challenge3()
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
        Code_challenge4()
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
        Activity10()
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
        Activity20()
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
        Activity25()
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
        Code_challenge16()
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
                Activity1()
                print("\n================================================================================")
                continue
                
        elif code.lower() == "a2":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 2")
                Activity2()
                print("\n================================================================================")
                continue

        elif code.lower() == "a3":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 3")
                Activity3()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a4":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 4")
                Activity4()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a5":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 5")
                Activity5()
                print("\n================================================================================")
                continue

        elif code.lower() == "a6":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 6")
                Activity6()
                print("\n================================================================================")
                continue

        elif code.lower() == "a7":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 7")
                Activity7()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a8":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 8")
                Activity8()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a9":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 9")
                Activity9()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a10":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 10")
                Activity10()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a11":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 11")
                Activity11()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a12":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 12")
                Activity12()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a13":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 13")
                Activity13()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a14":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 14")
                Activity14()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a15":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 15")
                Activity15()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a16":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 16")
                Activity16()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a17":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 17")
                Activity17()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a18":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 18")
                Activity18()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a19":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 19")
                Activity19()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a20":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 20")
                Activity20()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a21":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 21")
                Activity21()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a22":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 22")
                Activity22()
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
                Activity24()
                print("\n================================================================================")
                continue
        
        elif code.lower() == "a25":
                os.system('cls')
                print("\n================================================================================")
                print("\nActivity 25")
                Activity25()
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
            Code_challenge1()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc2":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 2")
            Code_challenge2()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc3":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 3")
            Code_challenge3()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc4":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 4")
            Code_challenge4()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc5":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 5")
            Code_challenge5()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc6":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 6")
            Code_challenge6()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc7":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 7")
            Code_challenge7()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc8":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 8")
            Code_challenge8()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc9":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 9")
            Code_challenge9()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc10":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 10")
            Code_challenge10()
            print("\n================================================================================")
            continue

        elif code.lower() == "cc11":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 11")
            Code_challenge11()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc12":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 12")
            Code_challenge12()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc13":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 13")
            Code_challenge13()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc14":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 14")
            Code_challenge14()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc15":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 15")
            Code_challenge15()
            print("\n================================================================================")
            continue
            
        elif code.lower() == "cc16":
            os.system('cls')
            print("\n================================================================================")
            print("\nCode Challenge 16")
            Code_challenge16()
            print("\n================================================================================")
            continue

        elif code.lower() == "zero":
            main()

        else:
            print("Invalid Choice.")
            print("Type 'zero' to return to Main Menu.")
            main()
main()