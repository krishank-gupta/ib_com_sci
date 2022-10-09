# imports
from library.library import hashLine,centerVal,colorCodes as cc, validate_int, validate_int_between, validate_str, validate_date
from library.login import login, signup
import texttable as tt


# prints
loginOptions = ['1. Register', '2. Login']

print(f"""{cc['purple']}{hashLine}
#{"Hello and welcome to Crypty. Please register or login to continue.".center(centerVal-2)}#
# {loginOptions[0]}{"".center(centerVal-int(len(loginOptions[0]))-3)}#
# {loginOptions[1]}{"".center(centerVal-int(len(loginOptions[1]))-3)}#
{hashLine}{cc['end_code']}""")

def getUsername():
    return validate_str(f"{cc['blue']}Please enter username: {cc['end_code']}", "blue")

def getPswd():
    return validate_str(f"{cc['blue']}Please enter password: {cc['end_code']}", "blue")

def loginSystem():

    loginChoice = validate_int_between('Press 1 to register, 2 to login: ', 1,2, "blue")    

    if loginChoice == 1:
        registerMessage = f"""{cc['purple']}{hashLine}\n#{"Register".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal)
        # registerMessage = 'register'
        print(registerMessage)
        signup(getUsername(), getPswd())
        
        print(f"""{cc['green']}{hashLine}\n#{"Register Success".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

        return True
    
    elif loginChoice == 2:
        loginMessage = f"""{cc['purple']}{hashLine}\n#{"Login".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal)
        # loginMessage = 'login'
        print(loginMessage)

        while(login(getUsername(), getPswd()) == False):
            pass

        print(f"""{cc['green']}{hashLine}\n#{"Login Success".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

        return True

def menu():
    menuOptions = ["1. See description of USD Coin", "2. Enter a transaction", "3. Withdraw a transaction", "4. See all transaction", "5. Profit/loss calculator", "6. Exit"]

    menuOptionsPrint = (f"""{cc['purple']}{hashLine}\n#{"Choose an option.".center(centerVal-2)}#\n# {menuOptions[0]}{"".center(centerVal-int(len(menuOptions[0]))-3)}#\n# {menuOptions[1]}{"".center(centerVal-int(len(menuOptions[1]))-3)}#\n# {menuOptions[2]}{"".center(centerVal-int(len(menuOptions[2]))-3)}#\n# {menuOptions[3]}{"".center(centerVal-int(len(menuOptions[3]))-3)}#\n# {menuOptions[4]}{"".center(centerVal-int(len(menuOptions[4]))-3)}#\n# {menuOptions[5]}{"".center(centerVal-int(len(menuOptions[5]))-3)}#\n{hashLine}{cc['end_code']}""")

    print(menuOptionsPrint)
    menuChoice = validate_int_between('Choose an option: ', 1,6, "blue")    

    while(True):

        if menuChoice == 1:
            print("usd coin is a bs")

        if menuChoice == 2:
            print("enter a transaction")
            dateInput = (validate_date("Please enter date: (YYYY-MM-DD)", "purple"))
            descInput = (validate_str("Please enter description: ", "purple"))
            categoryOptions = ['1. Expense', '2. Income']
            categoryOptionsPrint = (f"""{cc['purple']}{hashLine}\n#{"Choose an option.".center(centerVal-2)}#\n# {categoryOptions[0]}{"".center(centerVal-int(len(categoryOptions[0]))-3)}#\n# {categoryOptions[1]}{"".center(centerVal-int(len(categoryOptions[1]))-3)}#\n{hashLine}{cc['end_code']}""")
            print(categoryOptionsPrint)
            categoryInput = (validate_int_between("Please enter category from option: ",1, len(categoryOptions), "purple"))
            amountInput = (validate_int("Please enter amount: ", "purple"))

            with open("data/transactions.csv", 'a') as f:
                f.write('\n')
                f.write(dateInput + ',')
                f.write(descInput + ',')
                f.write(categoryOptions[categoryInput-1] + ',')
                f.write(str(amountInput) + ' USD Coin')
            f.close()

            print(f"""{cc['green']}{hashLine}\n#{"Transaction Added Successfully".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))


        if menuChoice == 3:
            tb = tt.Texttable()
            updateTransactionRecordsList = []

            with open("data/transactions.csv", 'r') as file:
                transactionDb = file.readlines()

                while(len(transactionDb) != 0):
                    for idx,line in enumerate(transactionDb):
                        data = line.strip().split(",")
                        tb.header(["ID","Date", "Description", "Category", "Amount"])
                        tb.add_row([int(idx)+1,data[0],data[1], data[2],data[3]])
                        tb.set_cols_width([3,13-1,25-1,13-1,13])

                    tb.set_chars(['-', '#', '#', '='])
                    print(f"{cc['yellow']}{tb.draw()}\n{hashLine}{cc['end_code']}")

                    removeID = validate_int_between("Please enter the ID of transaction you wish to remove: ", 1, len(transactionDb), 'blue') - 1

                    for idx,line in enumerate(transactionDb):
                        if idx != removeID:
                            updateTransactionRecordsList.append(line)
            file.close()

            with open("data/transactions.csv", 'w') as empty_csv:
                pass

            with open("data/transactions.csv", 'a') as f:
                for i in updateTransactionRecordsList:
                    f.write(i)
            f.close()            

            print(f"""{cc['green']}{hashLine}\n#{"Transaction Removed Successfully".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

        if menuChoice == 4:
            tb = tt.Texttable()
            with open("data/transactions.csv", 'r') as file:
                transactionDb = file.readlines()
                print(f"""{cc['yellow']}{hashLine}\n#{"All data".center(centerVal-2)}#{cc['end_code']}""")
                for line in transactionDb:
                    data = line.strip().split(',')
                    tb.header(["Date", "Description", "Category", "Amount"])
                    tb.add_row([data[0],data[1], data[2],data[3]])
                    tb.set_cols_width([13-1,27-1,15-1,15])

                
            tb.set_chars(['-', '#', '#', '='])
            print(f"{cc['yellow']}{tb.draw()}\n{hashLine}{cc['end_code']}")
            file.close()

        if menuChoice == 5:

            tb = tt.Texttable()
            cashInHand = int(0)
            with open("data/transactions.csv", 'r') as file:
                transactionDb = file.readlines()
                # print(f"""{cc['yellow']}{hashLine}\n#{"All data".center(centerVal-2)}#{cc['end_code']}""")
                for line in transactionDb:
                    data = line.strip().split(',')
                    amount = int(str(data[3]).split(' ')[0])
                    tb.header(["Date", "Description", "Category", "Amount"])
                    if data[2] == '2. Income':
                        cashInHand += amount
                    elif data[2] == '1. Expense':
                        cashInHand -= amount
                    else:
                        print("error")
                
            if cashInHand > 0:
                print(f"""{cc['green']}{hashLine}\n#{f"Profit of {cashInHand}. Crypty suggests selling more USD Coin".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

            else:
                print(f"""{cc['red']}{hashLine}\n#{f"Loss of {cashInHand}. Crypty suggests buying more USD Coin".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

            file.close()            

        if menuChoice == 6:
            quit()
        
        print(menuOptionsPrint) 
        menuChoice = validate_int_between('Choose an option: ', 1,6, "blue")    
        
if(loginSystem() == True):
    menu()