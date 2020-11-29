#***************************************************************
#
#  Developer:         Chance Wylie
#
#  Program #:         Program 11
#
#  File Name:         Program11.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          December 1st 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter 5-9
#
#  Description:
#     This program is designed to determine the team that won the world series 
#     in a given year as well as the number of times they have won by utilizing python dictionaries
#***************************************************************


BASE_YEAR = 1903

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
file = "program11.txt"

def open_file():
 
    return open(file, 'r')
def make_dict(file_object):

    year_dict = {}
    line = file_object.readline().rstrip('\n')

    for i in range(BASE_YEAR, 2021):
        year_dict[i] = line
        line = file_object.readline().rstrip('\n')
    #print(year_dict, '\n')
    count_dict = {}
    for i in range(BASE_YEAR, 2020):
        team = year_dict[i]
        if not team in count_dict:
            count_dict[team] = 1
        else:
            count_dict[team] += 1
   #print(count_dict, '\n')
    return year_dict, count_dict

def showResults(year_dict, count_dict):
    valid = True
    while valid:
        try:
            year = int(input('Enter a year in the range from 1903 to 2020 to '
                             'know which team won World Series in the year or type 0 to quit: '))
            if year > 1902 and year < 2021 and year != 1904 and year != 1994:
                print('\n\nThe team that won the world series in',year,'is the', year_dict[year], '\n\nThey have won',count_dict[year_dict[year]], 'times\n')
            elif year == 1904:
                print('World Series Not Played in 1904')
            elif year == 1994:
                print('World Series Not Played in 1994')
            elif year == 0:
                valid = False
                print('Exiting')
                quit()
        except:
            print('Enter a year in integer.')
    
def main():
    developerInfo()
    file_object = open_file() 
    year_dict, count_dict = make_dict(file_object)
    showResults(year_dict, count_dict) 


    #winningTeamsList = readWinningTeam



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

