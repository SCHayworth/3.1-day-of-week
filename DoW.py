# 3-1 Day of the Week Program
# by Shaun Hayworth
# CIS 2
# 2019-10-01

# Prompts user to enter an integer between 1 and 7, and displays a day of the week
# corresponding with the input.

# Initialize the check_day boolean variable and set it to True
check_day = True

while check_day == True:
    # Prompt user for input and store it in the day_of_week variable
    day_of_week = int(input('Please enter a number between 1 and 7: '))

    # To be done:
    #   Check for valid integer
    #   Check for valid range

    # Display name of day corresponding with input, or an error message if input is inappropriate.
    if day_of_week == 1:
        print('Monday')
    elif day_of_week == 2:
        print('Tuesday')
    elif day_of_week == 3:
        print('Wednesday')
    elif day_of_week == 4:
        print('Thursday')
    elif day_of_week == 5:
        print('Friday')
    elif day_of_week == 6:
        print('Saturday')
    elif day_of_week == 7:
        print('Sunday')
    else:
        print('That is not a valid day.')
          
    # Ask user if they'd like to enter another day.
    another_day = char(input('Would you like to enter a new day (y/n)? '))
    
    # Run the program again if yes, or else set check_day to False.
    if another_day == n or N:
        check_day = False
else:
    print('Goodbye!)
        
