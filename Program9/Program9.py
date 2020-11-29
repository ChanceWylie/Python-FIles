#********************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         9
#
#  File Name:         Program9.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          11/2/20
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapters 5-7
#
#  Description:
#     This program takes the average rainfall for each month and then finds the annual
#     rainfall, total rainfall, highest rainfall for a month and lowest rainfall for a month.
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
    
    inFile = open('program9.txt', 'r')
    
    monthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                   'August', 'September', 'October', 'November', 'December']

    rainfallList = readFile(inFile, monthsList)

#***************************************************************
#
#  Function:     readFile
# 
#  Description:  This function reads the file and creates the list
#
#  Parameters:   Input file object, months list
#
#  Returns:      Rainfall list 
#
#**************************************************************
def readFile(inFile, monthsList):
    rainfallList = []
    idx = 0
    
    print("%-12s    %10s\n" % ("Month", "Rainfall"))
    
    lineRead = inFile.readline()       # Read first record
    while lineRead != '':              # While there are more records
       words = lineRead.split()        # Split the records into substrings
       annualRainfall = float(words[0])
       print("%-12s   %8.2f" % (monthsList[idx], annualRainfall))
       idx += 1
       rainfallList.append(annualRainfall)
       lineRead = inFile.readline()    # Read next record

    totalAnnual = findTotalAnnual(rainfallList)
    
    

    entries = len(rainfallList)
    avgRainfall = totalAnnual / entries
    
    maxRainfall = findLargest(rainfallList,entries)
    

    

    
    print('\nTotal rainfall for the year was {:.2f} inches'.format(totalAnnual)) 
    print('\nAverage rainfall for the year was {:.2f} inches'.format(avgRainfall)) 
    print('\nThe largest amount of rainfall was {:.2f} inches'.format(maxRainfall)) 
    print('\nThe smallest amount of rainfall was {:.2f} inches'.format(min(rainfallList))) 
       
    # Close the file.
    inFile.close() # Close file
    
    return rainfallList
#***************************************************************
#
#  Function:     findLargest
# 
#  Description:  This function reads the file and creates the list
#
#  Parameters:   Input file object, months list
#
#  Returns:      Rainfall list 
#
#**************************************************************
def findLargest (arr, n):
    max = arr[0]
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max


#***************************************************************
#
#  Function:     findTotalAnnual
# 
#  Description:  finds the amount of annual rainfall
#
#  Parameters:   None
#
#  Returns:      max 
#
#**************************************************************
def findTotalAnnual(arr):
    totalAnnual = 0
    for months in arr:
        totalAnnual += months
    return(totalAnnual)
    
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
    print('Program:  Nine')
    print()
    # End of the developerInfo function

# Call the main function.
main()
