#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 1
#
#  File Name:         Program1.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          9/08/2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 1
#
#  Description:
#   this is my first programming assignment at ACC
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
    
    amount = 32500.00

    
    twiceMonth = amount / 6
    biWeekly = amount / 26
    
    print('Annual Salary           = ', amount)
    print('When paid twice a month = ', twiceMonth)
    print('When paid bi-weekly     = ', biWeekly)
    
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
    print('Name:     Chance Wylie')
    print('Course:   Programming Fundamentals I')
    print('Program:  One')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
