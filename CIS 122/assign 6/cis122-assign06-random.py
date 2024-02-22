# CIS 122 spring 2021 assign 6 random
# Author: Hunter McMahon
# Partner: completed solo
# Description: youll never be able to guess what numbers come out becuase heck even i dont know what numbers will be output

#import the padding functions and os 
from cis122_assign06_shared import pad_left, pad_right
import os

def random_num_math():
    """
    handles the calculations of several stats of the numbers in a text file
        uses loops to pull values from an external file and commputate the total and average along with distinguish numbers from comments
    Args
    none
    Returns:
    none the fucntion is void
    """
    #establish variables for the computations
    comments = 0
    count = 0
    total = 0
    average = 0

    #spacing for the print latter
    label_spacing = 10
    num_spacing = 10

    #import the text file
    #while loop to open file and run computations
    fin = 0
    while fin == 0:
        inputfile = input('Enter filename (blank to exit): ')
        inputfile = inputfile.strip() 
        if len(inputfile) == 0:
            break
        elif len(inputfile) > 0:
            isvalid = os.path.isfile(inputfile)
            if isvalid ==True:
                fin = open(inputfile)
                #create a loop to pull all the numbers from the files, and do the math
                for line in fin:
                    raw = line.strip()
                    if raw[0] == '#':
                    #determines if the line is a comment
                        comments += 1
                    else:
                        #if the line isnt a comment then the other variables are updated
                        raw = int(raw)
                        count += 1
                        total += raw
                        average = round(total/count, 2)
                fin.close()
                fin = 0
                #prints the final results
                print(pad_right('Count:', label_spacing) + pad_left(str(count), num_spacing) + '\n' + pad_right('Comments:', label_spacing) + pad_left(str(comments), num_spacing) +'\n' + pad_right('Total:', label_spacing) + pad_left(str(total), num_spacing) + '\n' + pad_right('Average:', label_spacing) + pad_left(str(average), num_spacing))
            else:
                print('Invalid filename: ' + inputfile)
random_num_math()
