# Quiz 011

# Input with validation. Input must be a whole number and be between 1 and 12
while True:
  inputMonth = input("Please enter a month number: (1-12) ")
  try:
    inputMonth = int(inputMonth)
    if inputMonth > 0 and inputMonth <= 12:
      break;
    else:
      print(f"You entered {inputMonth}. This is not a number between 1 and 12. Please enter a number between 1 and 12")
  except ValueError:
    try:
      float(inputMonth)
      print(f"You entered {inputMonth}. This is not a whole number. Please enter a whole number")
    except ValueError:
      print(f"You entered {inputMonth}. Please enter a number")

# List of months and days
monthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# List of lengths of months
lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
# List of the first day of a month 
startDays = [7,3,3,6,1,4,6,2,5,7,3,5]

# Terminal output style codes
end_code = "\033[00m"
green = "\033[0;32m"
red = "\33[0;31m"

# Terminal output length
centerLength = 26

# Main function
def daysOfMonth(month): 

  # Index variables
  indexOfMonth = monthsList.index(month)
  monthLength = lengths[indexOfMonth]
  firstDayNum = startDays[indexOfMonth]-1 
  dayNum = firstDayNum
  year = f"{month} 2022"
  daysArr = [];

  # Loop 8th day back to first because 7 days in a week
  for i in range(1, monthLength + 1, 1):
    dayName = days[dayNum]

    # If two digits
    if i > 9:
      daysArr.append(i)
    # If one digit add a empty space before number
    else:
      daysArr.append(f" {i}")

    # day 8 becomes the same day as day 1
    if dayNum+1 > 6:
      dayNum -= 7
    dayNum += 1

  #Insert empty spaces in array to get first day under the day
  for i in range(0,firstDayNum,1):
    daysArr.insert(0, "  ")
  
  # split days by 7 to get array of weeks
  daysArrSplit = [daysArr[i:i + 7] for i in range(0, len(daysArr), 7)]

  #add empty spaces at the end
  emptySpaceEnd = ((len(daysArrSplit) * 7) - (daysArr[len(daysArr)-1] + firstDayNum))
  for i in range(0, emptySpaceEnd, 1):
    daysArr.append("  ")

  # Update daysArr after adding empty spaces at the end
  daysArrSplit=[daysArr[i:i + 7] for i in range(0, len(daysArr), 7)]

  # Print
  print(f"""{red}{centerLength * '#'}\n#{year.center(centerLength-2)}#\n#{ 'Su Mo Tu We Th Fr Sa'.center(centerLength-2)}#{end_code}""")
  for i in range(0, len(daysArrSplit), 1):
    print(f"{red}#{' '.join(str(e) for e in daysArrSplit[i]).center(centerLength-2)}#{end_code}")
  print(f"{red}{centerLength * '#'}{end_code}")
  
# Call function
daysOfMonth(monthsList[inputMonth-1])