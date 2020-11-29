#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 2
#
#  File Name:         Program2.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          9/11/2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 2
#
#  Description:
#     The Program calculates the averages of the five integer scores and prints them
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    a = int(input('Enter your first score: '))
    b = int(input('Enter your second score: '))
    c = int(input('Enter third score: '))
    d = int(input('Enter fourth score: '))
    e = int(input('Enter fifth score: '))

    Avg = (a + b + c + d + e) / 5
    
    
    print('The value of a is: ', format(Avg, '.2f'))
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:    Chance Wylie')
    print('Course:   Programming Fundamentals I')
    print('Program:  Two')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 2
