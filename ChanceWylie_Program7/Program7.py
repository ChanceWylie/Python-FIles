#********************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         7
#
#  File Name:         Program7.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          10/18/2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter 4 and Chapter 6
#
#  Description:
#     This program calculates a faculty member's
#     new gross pay.
#********************************************************************

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
    
    inFile = open('Program7.txt', 'r')
    total = 0
    newSalaryTotal = 0
    facCount = 0
    raiseTotal = 0
    lineRead = inFile.readline()
    while lineRead != '':
       numberList = lineRead.split()
       for number in numberList:
          salary = float(number)
          if salary > 60000.0:
              newSalary = salary * 1.04
              newSalaryTotal += newSalary
              payRaise = newSalary - salary
              total = total + salary
              raiseTotal = raiseTotal + payRaise
              facCount+=1
              print('Faculty Number:',facCount)
              print('Old Salary: ', format(salary,'.2f'), sep = '$')
              print('Raise: ', format(payRaise, '.2f'), sep = '$')
              print('New Salary: ', format(newSalary,'.2f'), sep = '$')
              print('')
            
          elif salary > 50000.0:
              newSalary = salary * 1.07
              newSalaryTotal += newSalary
              payRaise = newSalary - salary
              total = total + salary
              raiseTotal = raiseTotal + payRaise
              facCount+=1
              print('Faculty Number:',facCount)
              print('Old Salary: ', format(salary,'.2f'), sep = '$')
              print('Raise: ', format(payRaise, '.2f'), sep = '$')
              print('New Salary: ', format(newSalary,'.2f'), sep = '$')
              print('')
              
          elif salary <= 50000.0:
              newSalary = salary * 1.055
              newSalaryTotal += newSalary
              payRaise = newSalary - salary
              total = total + salary
              raiseTotal = raiseTotal + payRaise
              facCount+=1
              print('Faculty Number:',facCount)
              print('Old Salary: ', format(salary,'.2f'), sep = '$')
              print('Raise: ', format(payRaise, '.2f'), sep = '$')
              print('New Salary: ', format(newSalary,'.2f'), sep = '$')
              print('')
              
              
          
          
          
       lineRead = inFile.readline()
    averageRaise = raiseTotal / 22
    averageSal = total / 22
    averageNewSal = newSalaryTotal / 22
    print('Sum of raises: ', format(raiseTotal,'.2f'), sep = '$')   
    print('Sum of old salaries: ', format(total,'.2f'), sep = '$')
    print('Sum of new salaries: ', format(newSalaryTotal,'.2f'), sep = '$')
    print('Average of raises: ', format(averageRaise,'.2f'), sep = '$')
    print('Average of old salaries: ', format(averageSal,'.2f'), sep = '$')
    print('Average of the new salaries: ', format(averageNewSal,'.2f'), sep = '$')
    # Close the file.
    inFile.close()
    
# Call the main function.

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
   print('Program:  Seven')
   print('')
   print('This program is designed to calculate a faculty members new gross pay')
   print('')
    # End of the developerInfo function

main()
