#***************************************************************
#
#  Function:     showResults
# 
#  Description:  This function displays the results.
#                Please do NOT modify this function.  If you do,
#                you will not receive credit for Program 11.
#
#  Parameters:   None
#
#  Returns:      Nothing 

#**************************************************************
def showResults(year, year_dict, count_dict):
    year = int(input('Enter a year in the range 1903-2020:' ))
    # Print results
    if year == 1904 or year == 1994:
        print("\nThe world series wasn't played in the year", year)
    elif year < 1903 or year > 2020:
        print('\nThe data for the year', year, 
              'is not included in our database.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print('\nThe team that won the world series in ', \
              year, ' is the ', winner, '.', sep='')
        if wins > 1:
           print('They have won the world series', wins, 'times.')
        else:
           print('They have won the world series', wins, 'time.')

    print()
# End of showResults function
