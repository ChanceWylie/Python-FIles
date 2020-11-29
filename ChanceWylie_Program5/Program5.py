#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 5
#
#  File Name:         Program5.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          9/28/2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 2
#
#  Description:
#     This program is used to calculate what discount you get when you spend money on units
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
unitsSold = int(input('How many units did you sell? '))
retailPrice = 99


if unitsSold >= 100:
  discount = .50
if unitsSold <= 99:
  discount = .40
if unitsSold <= 69:
  discount = .35
if unitsSold <= 49:
  discount = .30
if unitsSold <= 19:
  discount = .20
if unitsSold < 10:
  discount = 0

discountApplied = 1 - discount
totalCost = unitsSold * retailPrice * discountApplied
Savings = unitsSold * retailPrice - totalCost
print('Discount applied is: ', format(discount, ',.0%'))
print('Total Savings due to discount is: ', format(Savings , ',.2f'), sep = '$')
print('The total cost of the purchase is: ', format(totalCost , ',.2f'), sep = '$')



    
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
    print('Program:  Five')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
