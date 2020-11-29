#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 12
#
#  File Name:         Program12.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          December 10th, 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter 6-10
#
#  Description:
#     This program is designed to implement classes and to instantiate and
#     manipulate python objects to calculate a monthly net pay for an employee
#     given weekly salaries
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
import Employeeclass

def main():
    developerInfo()
    flag = ''
    while flag != 'no':
        name = input('What is your full name? ')
        rate = float(input('What is your hourly pay rate? '))


        employeeObject = Employeeclass.Employee()
        employeeObject.__init__()
        employeeObject.set_name(name)
        employeeObject.get_name()
        employeeObject.set_rate(rate)
        employeeObject.get_rate()
        temp = 1
        for x in range(4):
            hoursWorked = int(input('How many hours have you worked for week ' + str(temp)+' '))
            employeeObject.set_hours_worked(hoursWorked)
            temp+=1
        employeeObject.get_hours_worked()
        employeeObject.get_regular_pay()
        employeeObject.get_overtime_pay()
        employeeObject.get_gross_pay()
        employeeObject.get_tax()
        employeeObject.get_net_pay
        print(employeeObject.__str__())
        flag = input('Do you want to continue <yes/no>? ')
        if flag == 'no':
            break
    print('Program Closing')
    
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
    print('Program:  Eleven')
    print()
    # End of the developerInfo function

# Call the main function.
main()

