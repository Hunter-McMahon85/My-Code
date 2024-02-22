# CIS 122 spring 2021 Assign 4 v1
# Author: Hunter McMahon
# Partner: completed solo 
# Description: whats the date? seriously, what day is it, i just know the year and the total for some reason

"""
outline
1. use the input function to ask the user for an input for day and year and assign these values to a variable
2. import the is_leap_year() function from lab 4 
3. check to see if the year is valid (year>0), if not it will output an error message
4. call the is_leap_year() function for the inputed year to get a boolean value & assign to variable
5. write a function to check if the day is valid, if not it will output an error message
6. if both the day and the year are valid, code will move on to a function to give the date,
7. write the code to determine what month of the year it is based on conditionals and day of year, this will be dependent on whether or not the year is a leap year.
8. with the month determined, code will then need to be written to do math figure out what day of the month it is. 
9. now that the day month and year have been determined, they must be put together as a string and printed back to the user
"""
#step 1 take input
year = int(input('Enter year:'))
dayofyear = int(input('Enter the day of the year:'))

#step 2 leap year function
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
#step 3 check year validity
validyear = year>0
if validyear == False:
    print:('Year must be > 0')
    
#step 4 check for leap year
leapyear = is_leap_year(year)

#step 5 check if day is valid
dayvalidation = True
if leapyear == True:
    dayvalid = 366 >= dayofyear > 0
    if dayvalid == False:
        print('Day must be <= 366')
        dayvalidation = False
elif leapyear == False :
    dayvalid = 365 >= dayofyear > 0
    if dayvalid == False:
        print('Day must be <= 365')
        dayvalidation = False

            
#step 6,7,8, and 9
if validyear == True:
    if dayvalidation == True:
        if leapyear == True:
            if 31 >= dayofyear >= 1:
                print("January " + str(dayofyear)+ ', ' + str(year))
            elif 60 >= dayofyear >= 32:
                print("February " + str(dayofyear-31)+ ', ' + str(year))
            elif 91 >= dayofyear >= 61:
                print("March " + str(dayofyear-60)+ ', ' + str(year))
            elif 121 >= dayofyear >= 92:
                print("April " + str(dayofyear-91)+ ', ' + str(year))
            elif 152 >= dayofyear >= 122:
                print("May " + str(dayofyear-121)+ ', ' + str(year))
            elif 182 >= dayofyear >= 153:
                print("June " + str(dayofyear-152)+ ', ' + str(year))
            elif 213 >= dayofyear >= 183:
                print("July " + str(dayofyear-182)+ ', ' + str(year))
            elif 244 >= dayofyear >= 214:
                print("August " + str(dayofyear-213)+ ', ' + str(year))
            elif 274 >= dayofyear >= 245:
                print("September " + str(dayofyear-244)+ ',' + str(year))
            elif 305 >= dayofyear >= 275:
                print("October " + str(dayofyear-274)+ ', ' + str(year))
            elif 335 >= dayofyear >= 306:
                print("November " + str(dayofyear-305)+ ', ' + str(year))
            elif 366 >= dayofyear >= 336:
                print("December " + str(dayofyear-335)+ ', ' + str(year))
        elif leapyear == False:
            if 31 >= dayofyear >= 1:
                print("January " + str(dayofyear)+ ', ' + str(year))
            elif 59 >= dayofyear >= 32:
                print("Febuary " + str(dayofyear-31)+ ', ' + str(year))
            elif 90 >= dayofyear >= 60:
                print("March " + str(dayofyear-59)+ ', ' + str(year))
            elif 120 >= dayofyear >= 91:
                print("April " + str(dayofyear-90)+ ', ' + str(year))
            elif 151 >= dayofyear >= 121:
                print("May " + str(dayofyear-120)+ ', ' + str(year))
            elif 181 >= dayofyear >= 152:
                print("June " + str(dayofyear-151)+ ', ' + str(year))
            elif 212 >= dayofyear >= 182:
                print("July " + str(dayofyear-181)+ ', ' + str(year))
            elif 243 >= dayofyear >= 213:
                print("August " + str(dayofyear-212)+ ', ' + str(year))
            elif 273 >= dayofyear >= 244:
                print("September " + str(dayofyear-243)+ ', ' + str(year))
            elif 304 >= dayofyear >= 274:
                print("October " + str(dayofyear-273)+ ', ' + str(year))
            elif 334 >= dayofyear >= 305:
                print("November " + str(dayofyear-304)+ ', ' + str(year))
            elif 365 >= dayofyear >= 335:
                print("December " + str(dayofyear-334)+ ', ' + str(year))
