# CIS 122 spring 2021 Assign 4 v2
# Author: Hunter McMahon
# Partner: completed solo 
# Description: whats the date? seriously, what day is it, i just know the year and the total for some reason.

def start():
    months = 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',  'December'
    def is_leap_year(year_num):
        """
        determines if an inputed year is a leap year 
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year_num (int): the number of the year thats being tested to see if its a leap year
        Returns:
        True: year is a leap year
        False: year isnt a leap year
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
    
    def valid_year(year):
        """
        determines if a given year is valid using a conditional
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the number of the year thats being tested to see if its a valid year
        Returns:
        True: year is valid
        False: year is invalid
        """
        if year > 0:
            return True
        elif 0>=year :
            print('Year must be > 0')
            return False

    def valid_day_of_year(year, day_of_year):
        """
        determines if the inputed day is valid
            uses conditionals to test if a given day in a given year is valid, the year input is used to see if the day is in a leap year
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the year the day lies in, this is used to determine if the day lies in a leap year
        day_of_year (int): the day of the year thats being tested to see if its valid
        Returns:
        True: day is valid
        False: day is invalid
        """
        leapyear = is_leap_year(year)
        if leapyear == True:
            dayvalid = 366 >= day_of_year > 0
            if dayvalid == False:
                print('Day must be <= 366')
                return False
            else:
                return True
        elif leapyear == False :
            dayvalid = 365 >= day_of_year > 0
            if dayvalid == False:
                print('Day must be <= 365')
                return False
            else:
                return True
            
    #inputs  
    def input_year():
        """
        takes user input for the year
            takes input for the year and converts it into an integer and test to see if its valid
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        none
        Returns:
        year: the value given by the user in input if its valid
        0: the returned value if the year is invalid 
        """
        year = int((input('Enter year:')))
        if valid_year(year) == True:
            return year
        elif valid_year(year) == False:
            return 0
        
    def input_day_of_year(year):
        """
        takes the user input for the day of the year
            takes the user input for a day in the year and determines if it is valid
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the year the day lies in
        Returns:
        day_of_year: value entered by the user, returned if it is valid 
        0: the returned value if the day is invalid 
        """
        day_of_year = int((input('Enter the day of the year:')))
        if valid_year(year) == True:
            validday = valid_day_of_year(year, day_of_year)
            if validday == True:
                day_of_year = day_of_year
            elif validday == False:
                day_of_year = 0
        return day_of_year

    def get_days_in_year(year):
        """
        determines the # of days in a year
            determines the total # of days in the year depending on whether or not its a leap year
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the input year
        Returns:
        days: will either be 0 (if year is invalid), 365 or 366 (for leap year) and is the number of days in entered year
        """
        days = 0
        is_leap = is_leap_year(year)
        if valid_year(year) == True:
            if is_leap == True:
                days = 366
            elif is_leap == False:
                 days = 365
        else:
            days = days
        return days
    
    def valid_month(month):
        """
        checks to see if a given month is valid
            checks if a given month is valid based on an inputed number 1-12
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        month (int): the number of the month
        Returns:
        True: month is valid
        False: month is valid
        """
        if 12>= month > 0:
            return True
        elif month < 0:
            print("Month must be > 0")
            return False
        elif month > 12:
            print("Month must be <= 12")
            return False
        
    
    def translate_month(month):
        """
        takes an input to determine the month
            determines the month number based on some conditionals, saves it to a global variable and returns an string of the name of the month (empty if invalid)
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        month (int): really just day_of_year, determines what month it is
        Returns:
        month[monthnum-1] : month is a Tuple with the month name strings, [monthnum-1] makes sure the correct zIndex of the needed month is returned 
        '': the returned value if the month is invalid 
        """
        monthnum = 0
        leapyear = get_days_in_year(year)
        if leapyear == 366:
            if 31 >= month >= 1:
                monthnum = 1
            elif 60 >= month >= 32:
                monthnum = 2
            elif 91 >= month >= 61:
                monthnum = 3
            elif 121 >= month >= 92:
                monthnum = 4
            elif 152 >= month >= 122:
                monthnum = 5
            elif 182 >= month >= 153:
                monthnum = 6
            elif 213 >= month >= 183:
                monthnum = 7
            elif 244 >= month >= 214:
                monthnum = 8
            elif 274 >= month >= 245:
                monthnum = 9
            elif 305 >= month >= 275:
                monthnum = 10
            elif 335 >= month >= 306:
                monthnum = 11
            elif 366 >= month >= 336:
                monthnum = 12
            elif month > 366:
                monthnum = 13
        elif leapyear == 365:
            if 31 >= month  >= 1:
                monthnum = 1
            elif 59 >= month  >= 32:
                monthnum = 2
            elif 90 >= month  >= 60:
                monthnum = 3
            elif 120 >= month  >= 91:
                monthnum = 4
            elif 151 >= month  >= 121:
                monthnum = 5
            elif 181 >= month  >= 152:
                monthnum = 6
            elif 212 >= month  >= 182:
                monthnum = 7
            elif 243 >= month  >= 213:
                monthnum = 8
            elif 273 >= month  >= 244:
                monthnum = 9
            elif 304 >= month  >= 274:
                monthnum = 10
            elif 334 >= month  >= 305:
                monthnum = 11
            elif 365 >= month  >= 335:
                monthnum = 12
            elif month > 365:
                monthnum = 13
        months = 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',  'December'
        if valid_month(monthnum) == True:
            return months[monthnum-1]
        elif valid_month(monthnum) == False:
            return ''

    
    def get_days_in_month(year, month):
        """
        determines the day of the month
            determines day in the month based on leap year, and the month
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the current year (test to see if its a leap year)
        month (int): the number of days in the year (used to figure out how many days are in the month
        Returns:
        day: the day of the month, depends on what day of the year it is 
        """
        finder = months.index(month)+1
        day = 0
        if is_leap_year(year) == True:
            if finder == 1:
                day = day
            elif finder == 2:
                day = 31
            elif finder == 3:
                day = 60
            elif  finder == 4:
                day = 91
            elif finder == 5:
                day = 121
            elif finder == 6:
                day = 152
            elif finder == 7:
                day = 182
            elif finder == 8:
                day = 213
            elif finder == 9:
                day = 244
            elif finder == 10:
                day = 274
            elif finder == 11:
                day = 305
            elif finder == 12:
                day = 335
        elif is_leap_year(year) == False:
            if finder == 1:
                day = day
            elif finder == 2:
                day = 31
            elif finder == 3:
                day = 59
            elif finder == 4:
                day = 90
            elif finder == 5:
                day = 120
            elif finder == 6:
                day = 151
            elif finder == 7:
                day = 181
            elif finder == 8:
                day = 212
            elif finder == 9:
                day = 243
            elif finder == 10:
                day = 273
            elif finder == 11:
                day = 304
            elif finder == 12:
                day = 334
        return day
        
    #checks validity of a day
    def valid_day(year, month, day):
        """
        checks to make sure the year month and day is valid
            checks validity of inputs with their appropriate functions
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the current year (test to see if its a leap year)
        day (int): the day in the year
        month (int): the month number
        Returns:
        True: all of the inputs are valid
        False: one of the inputs is invalid
        """
        if valid_month(month) and valid_day_of_year(year, day) and valid_year(year) == True:
            return True
        elif valid_month(month) or valid_day_of_year(year, day) or valid_year(year) == False:
            return False
        
    def get_date_string(year, month, day):
        """
        makes a string of the current date
        takes input and makes a string of the current day based on the year and the day of year and the month
        Args:    <Each parameter, followed by type, colon, and a description of the paramter>
        year (int): the current year (test to see if its a leap year)
        month (int): the number of days in the year (used to figure out how many days are in the month
        day (int): the day of the month
        Returns:
        finalstring: the inputs compiled into a string that is the day of that year
        """
        daystring = str(day)
        yearstring = str(year)
        finalstring = ''
        if valid_day(year, months.index(month)+1, day) == True:
            finalstring = month + " " + daystring + ", " + yearstring 
        return finalstring
    
    year = input_year()
    day = input_day_of_year(year)
    month =translate_month(day)
    dayofmonth = day - get_days_in_month(year, month)
    print(get_date_string(year, month,  dayofmonth))
#call start
start()
