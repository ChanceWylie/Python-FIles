#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 4
#
#  File Name:         Program4.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          9/24/2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 3
#
#  Description:
#     This program is created to help simplify everything you need to know about your paycheck
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
    
idNumber = int(input('Enter your ID number: '))
hourlyRate = float(input('Enter your hourly rate: '))
weeklyHours = int(input('Enter how many hours you have worked for the week: '))
if weeklyHours>40:
    overtimeHours = weeklyHours - 40
    overtimePay = (overtimeHours) * hourlyRate * 1.5
    grossIncome = (40 * hourlyRate) + overtimePay
    regularHours = 40
    
elif weeklyHours<=40:
    grossIncome = weeklyHours * hourlyRate
    overtimeHours = 0
    overtimePay = 0
    regularHours = weeklyHours
totalHours = regularHours + overtimeHours
regularPay = (weeklyHours - overtimeHours)* hourlyRate
if grossIncome>600:
    Deductions = (grossIncome * .105) - 25
elif grossIncome<600:
    Deductions = 25
netPay = (overtimePay + regularPay) - Deductions
print('ID Number: ', idNumber)
print('Pay Rate: ', format(hourlyRate, ',.2f'), sep = '$')
print('Regular Hours: ', regularHours)
print('Overtime Hours: ', overtimeHours)
print('Total Hours: ', totalHours)
print('Regular Pay: ', format(regularPay, ',.2f'), sep = '$')
print('Overtime Pay: ', format(overtimePay, ',.2f'), sep = '$')
print("Gross Pay: ", format(grossIncome, ',.2f'), sep = '$')
print('Deductions: ', format(Deductions, ',.2f'), sep = '$')
print("Net Pay: ", format(netPay, ',.2f'), sep = '$')


    
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
    print('Program:  Four')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
