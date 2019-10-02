# 3-1 Day of the Week Program v. 2
# by Shaun Hayworth
# CIS 2
# 2019-10-01

# Prompts user to enter an integer between 1 and 7, and displays a day of the week
# corresponding with the input.

# This version of the program is built with the main code in a function, so that the program can be run multiple times without
# having to be re-initiated.

# Define the function, main(), which prompts the user for a number between 1 and 7, and prints the corresponding day to the screen.
# If the response is out of range, an error message is displayed.
def main():
    # Prompt user for input and store it in the day_of_week variable
    day_of_week = int(input('Please enter a number between 1 and 7: '))

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
        
# Asks the user if they would like to check another day, and if so, returns 1, or else returns 0.
def repeat_loop(repeat):
    check_again = str(input('Would you like to input another number (y/n)? '))
    if check_again == 'y' or 'Y':
        return 1
    else:
        return 0
        
# Initialize the check_day boolean variable and set it to 1.
check_day = 1

# Loop main() as long as the check_day variable is True, otherwise print a message to the screen and quit.
while check_day == 1:
    main()
    check_day = repeat_loop()
else:
    print('Goodbye!')
          
        
