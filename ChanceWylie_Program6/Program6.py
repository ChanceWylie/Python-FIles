#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 6
#
#  File Name:         Program6.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          10/11/2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 4
#
#  Description:
#     This program calculates a hotel's occupancy rate
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

    hotelFloors = int(input('How many floors does the hotel have?: '))
    print('')
    roomNum = 0
    roomOccupied = 0
    total = 0.0
    tempNum = 1
    while tempNum <= hotelFloors:
        tempRoomNum = int(input('Rooms on floor {}: '.format(tempNum)))
        tempRoomOccupied = int(input('Rooms occupied: '))
        roomNum+=tempRoomNum
        roomOccupied+=tempRoomOccupied
        print('')
        tempNum += 1
    occupancyRate = roomOccupied / roomNum
    print('The total rooms in the hotel is {} '.format(roomNum))
    print('The number of rooms occupied in the hotel is {} '.format(roomOccupied))
    roomUnoccupied = roomNum - roomOccupied
    print('The amount of rooms that are unoccupied in the hotel is {} '.format(roomUnoccupied))
    print('The occupancy rate for the hotel is', format(occupancyRate , ',.1%'))




    
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
    print('Program:  Six')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
