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

![system_diagram](/projects/digital_wallet/flowcharts/system-diagram.png)

## Flow Diagrams

Login System

![login_system](/projects/digital_wallet/flowcharts/login_system.png)


## Record of Tasks
| Task No | Planned Action             | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|----------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram      | To have a clear idea of the hardware and software requirements for the proposed solution | 15min         | September 22           | B         |
| 2       | Meet with client           | To have a list of things the ledger should be able to do approved by the client          | 15min         | September 23           | A         |
| 3       | Create description of coin | To have a clear description of USD Coin                                                  | 10min         | September 25           | A         |
| 4       | Decide tools to use        | To decide what tools like software will be best for the needs of the client              | 20min         | September 25           | A         |
| 5       | Create login system        | To have the ledger password protected for the user                                       | 20min         | September 28           | C         |

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