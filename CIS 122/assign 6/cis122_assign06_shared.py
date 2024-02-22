# CIS 122 spring 2021 assign 6 
# Author: Hunter McMahon
# Partner: completed solo
# Description: youll never be able to guess what numbers come out becuase heck even i dont know what numbers will be output

def pad_string(string, padsize, side = True, charecter = ' '):
    """
    takes multiple inputs to add padding to a string
        uses booleans and string/integer inputs to add padding to a string
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    side (boolean) deafaulted to true: determines the side of padding (true = left, false = right)
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    output_string = the padded string
    """
    output_string = ''
    if side == True:
        output_string = charecter*(padsize-len(string)) + string
    else:
        output_string = string + (charecter*(padsize-len(string))) 
    return output_string

def pad_left(string, size, charecter = ' '):
    """
    takes a string and ads a padding charecter to the left size times
        uses pad_string to add padding to the left side of a stirng
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    Padding = the padded string
    """
    padding = pad_string(str(string), size,  True, charecter)
    return padding

def pad_right(string, size, charecter = ' '):
    """
    takes a string and ads a padding charecter to the right by size times
        uses pad_string to add padding to the right side of a stirng
    Args
    string (str): the string were adding pading to
    padsize: (int): how many charecters of padding we want
    charecter (str) defualted to ' ': the charecter of the padding
    Returns:
    Padding = the padded string
    """
    padding = pad_string(str(string), size, False, charecter)
    return padding
