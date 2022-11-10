from library import validate_int,validate_int_between,validate_str

welcome_msg = "Welcome to the EV Calculator".center(50, "=")
prompt_msg = "Please enter an option [1-4]"

print(welcome_msg)
print("Options".center(50))

menu = """1. Average time per kWh
2. Total kWh
3. Total charge time
4. Show all data
"""
print(menu)

option = validate_int_between(prompt_msg,0,4)

with open("charging_log.csv", "r") as file:
    ev_logs = file.readlines()

if option == 3:
    index = 0
    total_time = 0
    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            time = values[2]
            test = time.split(":")
            print(test)
        index+=1
#option 2: Calculate total energy
if option == 2:
    index = 0
    total_energy = 0
    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            date = values[0]
            energy = values[1]
            time = values[2]
            total_energy += float(energy[0:5])
        index += 1
    print(f"The total energy charged is {total_energy}kWh")

#option 4: show all data
if option  == 4:
    print("4. Showing all data")
    index = 0
    for log in ev_logs:
        if index>0:
            print(f"No.{index}: {log}", end="") #strip removes the \n at the end of the line
        index += 1
