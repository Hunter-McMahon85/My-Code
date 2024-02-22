# CIS 122 spring 2021 Lab 4
# Author: Hunter McMahon
# Partner: completed solo during lab with GE luis
# Description: whats the date?

#month function
def get_full_month(num):
    """
    takes an integer input and if it coresponds to a month the function returns the name of the month
    Args
    num: (int): number to be compared to determine the month
    Returns:
    if the number is within the intervall [1, 12] the month corresponding will be returned
    ie. 1 = january, 2 = febuary, etc.
    if num is outside of that interval then an string describing the input as invalid is printed and a blank string returned
    """
    if num == 1:
        return "January"
    elif num == 2:
        return "February"
    elif num == 3:
        return "March"
    elif num == 4:
        return "April"
    elif num == 5:
        return "May"
    elif num == 6:
        return "June"
    elif num == 7:
        return "July"
    elif num == 8:
        return "August"
    elif num == 9:
        return "September"
    elif num == 10:
        return "October"
    elif num == 11:
        return "November"
    elif num == 12:
        return "December"
    else:
        print("Must be an integer between 1 and 12 (" + str(num) + " is invalid).")
        return ""

#test month function
def test_get_full_month():
    """
    test the get_full_month function using a for loop
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    none
    Returns:None
    """
    for i in range(14):
        month = get_full_month(i)
        if month != "":
            print(i, month)

#leap year function
def is_leap_year(year_num):
    """
    determines if a given year is a leap year
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    year_num: (int) the number of the year thats being tested to see if its a leap year
    Returns:
    true: year is a leap year
    false: year isnt a leap year
    """
    over_four = year_num%4
    over_hundy = year_num%100
    over_fourhundy = year_num%400
    if over_four == 0:
        if over_hundy == 0:
            if over_fourhundy == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#test for the leap years
def test_is_leap_year(start_year, end_year):
    """
    test a interval of years to see which ones are leap years using a for loop and the is_leap_year funtction. 
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    start_year: (int) start year of the interval
    end_year: (int) end year of the interval 
    Returns:None
    """
    for i in range(start_year, end_year + 1):
        if is_leap_year(i):
            print(i, end = ",")
    print()

#test calls
test_get_full_month()
test_is_leap_year(1996, 2112)






