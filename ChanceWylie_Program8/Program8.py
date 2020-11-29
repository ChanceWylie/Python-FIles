#********************************************************************
#
#  Developer:         Chance Wylie  
#
#  Program #:         Program 8
#
#  File Name:         Program8.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          October 23, 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter 5
#
#  Description:
#     This program is designed to calculate the solutions
#     and the discrimnate from a quadratic equation
#********************************************************************

import math
import Disc

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

    
    coeffA = int(input('Enter the coefficient A: '))
    if coeffA == 0:
        raise Exception("coefficient 'A' cannot be 0")
    coeffB = int(input('Enter the coefficient B: '))
    coeffC = int(input('Enter the coefficient C: '))
    
    disc = Disc.discriminant(coeffA, coeffB, coeffC)
   
    if disc>0:
        sol1 = (-coeffB-math.sqrt(disc))/(2*coeffA)
        sol2 = (-coeffB+math.sqrt(disc))/(2*coeffA)
        print("\nEquations has two real roots. "'\nx1 = ',format(sol1,'.2f') ,'\nx2 = ', format(sol2,'.2f'))
    elif disc==0:
        sol1=-coeffB/(2*coeffA)
        print('\nThe equation has one real root.''\nx1 = ',format(sol1,'.2f'))
    else:
        print("\nNo real roots")
    print('\nThe discriminant is: ', format(disc,'.2f'))
   # End of the main function

main()

# End of Program 8
