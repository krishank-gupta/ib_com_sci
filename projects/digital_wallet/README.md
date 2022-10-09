# Crypto Wallet

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

An example of the data stored is 

| Date | Description | Category | Amount  |
|------|-------------|----------|---------|
| Sep 23 2022 | bought a house | Expenses | 10 BTC |
| Sep 24 2022 | food for house celebration | Food | 0.000001 BTC |

## Proposed Solution

### Design statement:
I will to design and make a digital ledger for a client who is Ms. Sato The digital ledger will be about USD Coin and is constructed using the software Python. It will take  3-4 weeks to make and will be evaluated according to the following success criteria.

### Description of Cryptocurrency:
USD Coin is a digital stablecoin that was pegged to the United States dollar. USD Coin is managed by a consortium called Centre, which was founded by Circle and includes members from the cryptocurrency exchange Coinbase and Bitcoin mining company Bitmain, an investor in Circle.

### Description of my software:
This software is called Crypty. It is used to track transactions of the cryptocurrency USD Coin as per my client's needs. It lets the user create an account or login. It then lets the user enter a transaction, remove a transaction, see all past transactions, see profits or losses depending on entered transactions, and presents all these information in an easy to understand manner. All system messages are displayed in purple. Success messages and error messages are displayed in green and red respectively. Messages were an input is required from the user is displayed in blue color. All messages are displayed inside boxes to make it clear and easy to understand.

### Justification:
For this software, I will be using Python 3.10.6. I will be running it on Visual Studio Code 1.71.2 on a Mac OS Big Sur. I will be using Python because my client needs a software that will be based on the terminal and can be run without internet. Python can easily run on the terminal without the use of internet. Additionally, my client needed the software to be password protected. Using python I can easily make a login/signup system that can password protect and encrypt sensitive information that my user will enter. Furthermore, Python is easy and fast, and the amount of libraries python has makes any task possible. The use of libraries not only expands the scope of python, but also helps in making the development process faster and making the user experience much better. I will run Python on Visual Studio Code as I have been using VS Code for years now and am very comfortable using it. The VS Code extensions I have makes my development process faster and makes debugging simple. Additionally, VS Code runs my software in lightning speed. The reason I will use a Mac OS is because I own a MacBook Air. However, it can easily be runned on windows or linux.


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger calculates important data and shows the data using graphs.
5. The electronic ledger gives statistics including profit/loss and suggests to buy/sell.
6. The electronic ledger prints losses in red color, profits in green color.

# Criteria B: Design

## System Diagram

![system_diagram](/projects/digital_wallet/img/system-diagram.png)

## Flow Diagrams

Login System

![login_system](/projects/digital_wallet/img/login_system.png)

See all transactions

![all_transactions_display](/projects/digital_wallet/img/see-transactions.png)

Profit Loss Calculator

![profit_loss_calc](/projects/digital_wallet/img/profit-loss-calc.png)

## Record of Tasks

| Task No | Planned Action                | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|-------------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram         | To have a clear idea of the hardware and software requirements for the proposed solution | 15min         | September 22           | B         |
| 2       | Meet with client              | To have a list of things the ledger should be able to do approved by the client          | 15min         | September 23           | A         |
| 3       | Create description of coin    | To have a clear description of USD Coin                                                  | 10min         | September 25           | A         |
| 4       | Decide tools to use           | To decide what tools like software will be best for the needs of the client              | 20min         | September 25           | A         |
| 5       | Create login system           | To have the ledger password protected for the user                                       | 20min         | September 28           | C         |
| 6       | Create menu                   | To have the menu of options displayed after successful login                             | 3hr           | October 5              | C         |
| 7       | Design Profit/Loss Calculator | To have the software calculate profits and losses based on transaction records           | 20min         | October 2              | C         |
| 8       | Add flowcharts                | To draw flocharts of some essential processes in the software                            | 20min         | October 4              | B         |
| 9       | Add code snippets             | To show proof of usage of functions, loops, conditions, validation, etc                  | 20min         | October 7              | C         |
| 10      | Add testing                   | To have a list of action and expected outcomes for tester                                | 30min         | October 7              | B         |
| 11      | Add sources                   | To credit the usage of code written by other people                                      | 10min         | October 7              | C         |
| 12      | Git push!                     | Upload project to github                                                                 | 5min          | October 9              | C         |

## Testing

Testing any software is a very important step in the creation of the software. In most cases, testing is done by a person who is neither the client nor the developer so they can test all cases of the software without having any biases and having enough knowledge to test properly. This prevents crashed and bugs after the software's launch. To test my software, I have created a table of inputs and expected outputs.

| Number |                          Action                         |                                          Expected output                                          |
|:------:|:-------------------------------------------------------:|:-------------------------------------------------------------------------------------------------:|
|    1   | Multiple registrations.                                 | Multiple successful registrations. Notes: Try to match one username with another user's password. |
|    2   | Enter unexpected input for register/login options.      | Error message with clear message and how to fix.                                                  |
|    3   | Enter unexpected input for menu options.                | Error message with clear message and how to fix.                                                  |
|    4   | Test all menu options.                                  | As per menu options.                                                                              |
|    5   | Withdraw all transactions.                              | Pption to remove transaction disappears when last transaction is removed.                         |
|    6   | Add multiple transactions and check profit/loss system. | Losses print in red, profits print in green.                                                      |
|    7   | Test exit mode.                                         | Program quits.                                                                                    |


# Criteria C: Development

## Use of Git and Github

The entire software was coded from scratch using Visual Studio Code. Upon completion of every single task, git was updated. Code was uploaded to Github using the Github CLI. 

## Use of Loops

For and While loops were used throughout the software. An example is when reading csv file. I loop through every line in database and process the data.

```.py

for line in transactionDb:
    data = line.strip().split(',')
    tb.header(["Date", "Description", "Category", "Amount"])
    tb.add_row([data[0],data[1], data[2],data[3]])

```

## Use of Data Validation

All input datas had to be validated to prevent unhandled errors. I created a function that validated data according to the data type and saved it in the library file. Whenever I had to validate data, I called the function.

```.py
# library.py

def validate_int_between(msg, startNum, endNum, inputColor):
    while True:
        try:
            val = int(input(f"{cc[inputColor]}{msg}{cc['end_code']}"))
            if val >= startNum and val <= endNum:
                return val
            else:
                print(f"{cc['red']}Please enter a number between {startNum} and {endNum}{cc['end_code']}")
        except ValueError:
            print(f"{cc['red']}Please enter an integer{cc['end_code']}")
```
## Use of functions

Functions were used throughout the software. An example is in the login system, functions were used to process login or signup requests. These functions had the parameters of username and password. Signup function created an account using the params submitted and appended to the users.csv database. Login function took the params and crosschecked every line in the database to find a match. The function returned True if match was found and False if it wasn't.

```.py
signup(getUsername(), getPswd())

def signup(username, pswd):
    with open("credentials.csv", 'a') as f:
        f.write('\n')
        f.write(username + ',')
        f.write(pswd)
    f.close()

def login(username, pswd):
    with open("credentials.csv", 'r') as f:
        database = f.readlines()
        for line in database:
            stored_username, stored_pswd = line.strip().split(',')
            
            if username == stored_username and pswd == stored_pswd:
                return True

    f.close()

    print(f"{cc['red']}Username and password don't match!{cc['end_code']}")
    return False

```

# Video of working software
[![Watch the video](https://img.youtube.com/vi/ho77mAAGPVE/maxresdefault.jpg)](https://youtu.be/ho77mAAGPVE)

# Sources 

Code on how to remove row from csv file inspired by Serge de Gosson de Varennes on [stackoverflow](https://stackoverflow.com/a/33164330)

```.py
lines = list()
remove= [1,2,3,4]

with open('dataset1.csv', 'r') as read_file:
    reader = csv.reader(read_file)
    for row_number, row in enumerate(reader, start=1):
        if(row_number not in remove):
            lines.append(row)

with open('new_csv.csv', 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(lines)
```